package bigRTT;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.WritableComparable;

public class Traceroute implements WritableComparable<Traceroute>{

	private int hop;
	private String from;
	private double rtt;

	public Traceroute(){
	}
	
	public Traceroute(int hop, String from, double rtt) {
		this.hop= hop;
		this.from= from;
		this.rtt= rtt;
	}

	public int getHop() {
		return hop;
	}

	public void setHop(int hop) {
		this.hop = hop;
	}

	public String getFrom() {
		return from;
	}

	public void setFrom(String from) {
		this.from = from;
	}

	public double getRtt() {
		return rtt;
	}

	public void setRtt(double rtt) {
		this.rtt = rtt;
	}

	@Override
	public String toString() {
		return "[hop=" + hop + ", from=" + from + ", rtt=" + rtt + "]";
	}

	@Override
	public void readFields(DataInput in) throws IOException {
		this.hop = in.readInt();
		this.from = in.readUTF();
		this.rtt = in.readDouble();
	}

	@Override
	public void write(DataOutput out) throws IOException {
		out.writeInt(this.hop);
		out.writeUTF(this.from);
		out.writeDouble(this.rtt);
	}

	@Override
	public int compareTo(Traceroute o) {
		int result = o.getHop() - this.hop;
		if(result>0)
			return -1;
		if(result<0)
			return 1;
		return 0;
	}

}
