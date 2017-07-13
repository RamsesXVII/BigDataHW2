package jsonUtility;

import org.json.*;

public class JsonUtility {

	public JsonUtility(){
	}

	public boolean isJSONValid(String test) {
		try {
			new JSONObject(test);
		} catch (JSONException ex) {
			return false;
		}
		return true;
	}
}
