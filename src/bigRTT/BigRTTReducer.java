package bigRTT;


import java.io.IOException;
import java.util.Collections;
import java.util.LinkedList;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class BigRTTReducer extends
Reducer<Text, Traceroute, Text, Text> {


	@Override
	public void reduce(Text key, Iterable<Traceroute> values, Context context)
			throws IOException, InterruptedException {

		LinkedList<Traceroute> hopList = new LinkedList<>();

		for (Traceroute value : values) {
			Traceroute temp = new Traceroute(value.getHop(), value.getFrom(), value.getRtt());
			hopList.add(temp);
		}
		
		Collections.sort(hopList);
		
		for(int i=1; i < hopList.size() -1; i++){
			Traceroute central = hopList.get(i);
			Traceroute prev = hopList.get(i-1);
			Traceroute next = hopList.get(i+1);
			if ((central.getRtt() > prev.getRtt()) && (central.getRtt() > next.getRtt())){
				String result = "[" + prev.toString() + "," + central.toString() + "," + next.toString() + "]";
				double delta = central.getRtt() - next.getRtt();
				if (delta > 0.5) {
					String tracerouteKey = key.toString() + "-" + delta;
					context.write(new Text(tracerouteKey), new Text(result));
				}
			}
		}
	}
}

