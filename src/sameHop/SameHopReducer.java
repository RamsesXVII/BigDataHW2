package sameHop;


import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class SameHopReducer extends
Reducer<Text, Text, Text, Text> {

	private int results2 = 0;
	private int results3 = 0;


	@Override
	public void reduce(Text key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {

		int i=0;
		String valuesOutput= "";

		for(Text value : values){
			i++;
			valuesOutput+= "," + value.toString();
		}

		if(i==2)
			results2++;
		else
			results3++;

		context.write(key, new Text(valuesOutput));
	}

	@Override
	protected void cleanup(Context context) throws IOException, InterruptedException {
		context.write(new Text("2 different: " + results2 + " 3 different: " + results3), new Text(""));
	}
}

