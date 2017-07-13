package hopBloccanti;

import org.json.*;

import jsonUtility.JsonUtility;

import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class HopBloccantiMapper extends
Mapper<LongWritable, Text, Text, Text> {
	
	private JsonUtility jut = new JsonUtility();

	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {

		if(jut.isJSONValid(value.toString())){
			JSONObject obj = new JSONObject(value.toString());
			int probeId = obj.getInt("prb_id");
			int measurementId = obj.getInt("msm_id");
			String misurazione = probeId + "," + measurementId;
			JSONArray hopList= obj.getJSONArray("result");

			JSONObject finalHop = hopList.getJSONObject(hopList.length()-1);
			if (finalHop.getInt("hop")==255){

				boolean concluso = false;

				for (int i = hopList.length()-2; i>=0; i--){
					JSONObject singleHop = hopList.getJSONObject(i);

					if (concluso)
						break;

					if (singleHop.has("result")){
						JSONArray replies = singleHop.getJSONArray("result");

						for(int y=0; y < replies.length(); y++){
							JSONObject reply = replies.getJSONObject(y);
							if (reply.has("from")){
								context.write(new Text(reply.getString("from")), new Text(misurazione));
								concluso = true;
							}
							if (concluso)
								break;
						}
					}
				}
			}
		}
	}
}
