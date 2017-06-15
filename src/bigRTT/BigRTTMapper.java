package bigRTT;

import org.json.*;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class BigRTTMapper extends
Mapper<LongWritable, Text, Text, Traceroute> {

	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {

		JSONObject obj = new JSONObject(value.toString());

		int probeId = obj.getInt("prb_id");
		int measurementId = obj.getInt("msm_id");
		int endtime = obj.getInt("endtime");

		String tracerouteKey = probeId + "-" + measurementId + "-" + endtime;

		JSONArray hopList= obj.getJSONArray("result");

		for (int i = hopList.length()-1; i >=0; i--) {

			JSONObject singleHop = hopList.getJSONObject(i);
			JSONArray hopResults = singleHop.getJSONArray("result");
			double rtt = 0;
			String from = "";

			for (int y = 0; y < hopResults.length(); y++){
				JSONObject singleICMP = hopResults.getJSONObject(y);
				if(singleICMP.has("rtt")) {
					double singleRTT = singleICMP.getDouble("rtt");
					if (singleRTT > rtt){
						rtt = singleRTT;
						from = singleICMP.getString("from");
					}
				}
			}
			if(rtt!=0){
				Traceroute hop = new Traceroute(i+1, from, rtt);
				context.write(new Text(tracerouteKey), hop);
			}
		}
	}
}
