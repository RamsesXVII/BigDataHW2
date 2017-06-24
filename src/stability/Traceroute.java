package stability;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.WritableComparable;

public class Traceroute implements WritableComparable<Traceroute>{

	private String from;
	private int timeStamp;

	public Traceroute(){
	}

	public Traceroute(String from, int timeStamp) {
		this.from= from;
		this.timeStamp= timeStamp;
	}



	public String getFrom() {
		return from;
	}

	public void setFrom(String from) {
		this.from = from;
	}


	public int getTimeStamp() {
		return timeStamp;
	}

	public void setTimeStamp(int timeStamp) {
		this.timeStamp = timeStamp;
	}

	@Override
	public String toString() {
		return ";;;;;;;;;;;;;;" + from + "," + timeStamp;
	}

	@Override
	public void readFields(DataInput in) throws IOException {
		this.timeStamp= in.readInt();
		this.from = in.readUTF();
	}

	@Override
	public void write(DataOutput out) throws IOException {
		out.writeInt(this.timeStamp);
		out.writeUTF(this.from);
	}

	
	@Override
	public int compareTo(Traceroute o) {
		int result = o.getTimeStamp() - this.timeStamp;
		if(result>0)
			return -1;
		if(result<0)
			return 1;
		return 0;
	}
}
