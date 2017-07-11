package hopBloccanti;


import java.io.IOException;
import java.util.HashSet;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class HopBloccantiReducer extends
Reducer<Text, Text, Text, Text> {

	@Override
	public void reduce(Text key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {

		int sum = 0;
		HashSet<String> measuraments = new HashSet<>();

		for (Text value : values) {
			sum ++;
			String temp = value.toString();
			measuraments.add(temp);
		}
		
		String result = sum + "," + measuraments.size();
		context.write(key, new Text(result));
	}
}

