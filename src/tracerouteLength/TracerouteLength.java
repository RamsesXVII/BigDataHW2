package tracerouteLength;

import java.time.Instant;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapreduce.Job;

public class TracerouteLength {

	public static void main(String[] args) throws Exception {

		JobConf conf = new JobConf();
		conf.set("mapred.textoutputformat.separator", ",");
		
		FileInputFormat.addInputPath(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));
		
		Job job = Job.getInstance(conf, "tracerouteLength");
		job.setJarByClass(TracerouteLength.class);
		
		job.setMapperClass(TracerouteLengthMapper.class);
		job.setCombinerClass(TracerouteLengthReducer.class);
		job.setReducerClass(TracerouteLengthReducer.class);
		
		//job.setNumReduceTasks(3);

		job.setMapOutputKeyClass(IntWritable.class);
		job.setMapOutputValueClass(IntWritable.class);
		job.setOutputKeyClass(IntWritable.class);
		job.setOutputValueClass(IntWritable.class);
		
		long start = Instant.now().toEpochMilli();
		job.waitForCompletion(true);
		long end = Instant.now().toEpochMilli();
		System.out.println(end - start);
	}
}