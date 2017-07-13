package sameHop;

import org.json.*;

import jsonUtility.JsonUtility;

import java.io.IOException;
import java.util.HashSet;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class SameHopMapper extends
Mapper<LongWritable, Text, Text, Text> {

	private JsonUtility jut = new JsonUtility();
	
	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {

		if (jut.isJSONValid(value.toString())){
			JSONObject obj = new JSONObject(value.toString());

			String destination = obj.getString("dst_addr");
			int probeId = obj.getInt("prb_id");
			int measurementId = obj.getInt("msm_id");
			int endtime = obj.getInt("endtime");

			String tracerouteKey = probeId + "," + measurementId + "," + endtime + "," + destination;

			JSONArray hopList= obj.getJSONArray("result");

			for (int i = 0; i < hopList.length(); i++) {

				JSONObject singleHop = hopList.getJSONObject(i);

				if(singleHop.has("result")){
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
						int hop = i+1;

						for(String reply: replies)
							context.write(new Text(tracerouteKey + "," + hop + "," + hopList.length()), new Text(reply));
					}
				}
			}
		}
	}
}

