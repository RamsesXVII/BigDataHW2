package bigRTT;

import java.time.Instant;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapreduce.Job;

public class BigRTT {

	public static void main(String[] args) throws Exception {

		JobConf conf = new JobConf();
		conf.set("mapred.textoutputformat.separator", ",");
		FileInputFormat.addInputPath(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));
		
		Job job = Job.getInstance(conf, "bigRTT");
		job.setJarByClass(BigRTT.class);
		
		job.setMapperClass(BigRTTMapper.class);
		job.setReducerClass(BigRTTReducer.class);

		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Traceroute.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		long start = Instant.now().toEpochMilli();
		job.waitForCompletion(true);
		long end = Instant.now().toEpochMilli();
		System.out.println(end - start);
	}
}