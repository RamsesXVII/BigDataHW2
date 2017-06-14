package tracerouteLength;

import org.json.*;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class TracerouteLengthMapper extends
Mapper<LongWritable, Text, IntWritable, IntWritable> {
	
	private final IntWritable one = new IntWritable(1);

public void map(LongWritable key, Text value, Context context)
		throws IOException, InterruptedException {

	JSONObject obj = new JSONObject(value.toString());
	
	JSONArray hopList= obj.getJSONArray("result");
	IntWritable hopLength = new IntWritable(hopList.length());
	
	context.write(hopLength, one);
	}
}
