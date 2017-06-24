package stability;


import java.io.IOException;
import java.util.Collections;
import java.util.LinkedList;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class StabilityReducer extends
Reducer<Text, Traceroute, Text, Text> {


	@Override
	public void reduce(Text key, Iterable<Traceroute> values, Context context)
			throws IOException, InterruptedException {
		
		LinkedList<Traceroute> tracerouteList = new LinkedList<>();
		
		for(Traceroute t: values){
			Traceroute temp = new Traceroute(t.getFrom(), t.getTimeStamp());
			tracerouteList.add(temp);
		}
		
		Collections.sort(tracerouteList);
		
		for(int i=0; i<tracerouteList.size()-1;i++){
			Traceroute before = tracerouteList.get(i);
			Traceroute after = tracerouteList.get(i+1);
			if(!(before.getFrom().equals(after.getFrom())))
					context.write(key, new Text(before.toString() + ":::::::::" + after.toString()));
		}
			
	}
}

