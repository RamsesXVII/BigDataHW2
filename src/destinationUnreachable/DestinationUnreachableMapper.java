package destinationUnreachable;

import org.json.*;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class DestinationUnreachableMapper extends
Mapper<LongWritable, Text, Text, IntWritable> {
	
	private final IntWritable one = new IntWritable(1);
	
	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {
		
		JSONObject obj = new JSONObject(value.toString());
		
		JSONArray hopList= obj.getJSONArray("result");
		
		JSONObject finalHop = hopList.getJSONObject(hopList.length()-1);
		if (finalHop.getInt("hop")==255)
			for (int i = hopList.length()-2; i>=0; i--){
				JSONObject singleHop = hopList.getJSONObject(i);
				
				if (singleHop.has("result")){
					JSONArray replies = singleHop.getJSONArray("result");
					
					for(int y=0; y < replies.length(); y++){
						JSONObject reply = replies.getJSONObject(y);
						if (reply.has("from"))
							context.write(new Text(reply.getString("from")), one);
					}
				}
			}
				
	}
}

