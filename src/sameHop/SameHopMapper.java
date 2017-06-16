package sameHop;

import org.json.*;

import java.io.IOException;
import java.util.HashSet;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class SameHopMapper extends
Mapper<LongWritable, Text, Text, Text> {

	private int results2 = 0;
	private int results3 = 0;

	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {

		JSONObject obj = new JSONObject(value.toString());

		int probeId = obj.getInt("prb_id");
		int measurementId = obj.getInt("msm_id");
		int endtime = obj.getInt("endtime");

		String tracerouteKey = probeId + "-" + measurementId + "-" + endtime;

		JSONArray hopList= obj.getJSONArray("result");

		for (int i = 0; i < hopList.length(); i++) {

			JSONObject singleHop = hopList.getJSONObject(i);
			JSONArray hopResults = singleHop.getJSONArray("result");
			HashSet<String> replies = new HashSet<>();

			for(int y=0; y < hopResults.length(); y++){
				JSONObject echoReply = hopResults.getJSONObject(y);

				if(echoReply.has("from")){
					String ip = echoReply.getString("from");
					replies.add(ip);
				}
			}

			if (replies.size()>1){
				String valueOutput = replies.toString();
				int hop = i+1;
				context.write(new Text(tracerouteKey + "-" + hop + "-" + hopList.length()), new Text(valueOutput));

				if(replies.size()==2)
					results2++;
				else
					results3++;
			}
		}
	}


	@Override
	protected void cleanup(Context context) throws IOException, InterruptedException {
		context.write(new Text("2 different: " + results2 + " 3 different: " + results3), new Text(""));
	}

}

