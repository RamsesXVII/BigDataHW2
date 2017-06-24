package stability;

import org.json.*;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class StabilityMapper extends
Mapper<LongWritable, Text, Text, Traceroute> {

	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {

		JSONObject obj = new JSONObject(value.toString());

		String destination = obj.getString("dst_addr");
		int probeId = obj.getInt("prb_id");
		int measurementId = obj.getInt("msm_id");
		int endtime = obj.getInt("endtime");

		String tracerouteKey = probeId + "," + measurementId + "," + destination;

		JSONArray hopList= obj.getJSONArray("result");

		for (int i = 0; i < hopList.length(); i++) {
			JSONObject singleHop = hopList.getJSONObject(i);
			if(singleHop.has("result")) {
				int hop = singleHop.getInt("hop");
				JSONArray hopResults = singleHop.getJSONArray("result");

				for (int y = 0; y < hopResults.length(); y++){
					JSONObject singleICMP = hopResults.getJSONObject(y);
					if(singleICMP.has("from")) {
						int step = y+1;
						String hopKey = tracerouteKey + "," + hop + "," + step;
						Traceroute t = new Traceroute(singleICMP.getString("from"), endtime);
						context.write(new Text(hopKey), t);
					}
				}
			}
		}
	}
}
