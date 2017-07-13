package tracerouteLength;

import org.json.*;

import jsonUtility.JsonUtility;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class TracerouteLengthMapper extends
Mapper<LongWritable, Text, IntWritable, IntWritable> {

	private final IntWritable one = new IntWritable(1);
	private final IntWritable zero = new IntWritable(0);
	private JsonUtility jut = new JsonUtility();

	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {

		if (jut.isJSONValid(value.toString())){
			JSONObject obj = new JSONObject(value.toString());
			JSONArray hopList= obj.getJSONArray("result");
			JSONObject lastHop = hopList.getJSONObject(hopList.length()-1);

			if (!(lastHop.has("hop")))
				context.write(zero, zero);
			else {
				int finalHop = lastHop.getInt("hop");
				IntWritable hopLength = new IntWritable(finalHop);

				context.write(hopLength, one);
			}
		}
	}
}
