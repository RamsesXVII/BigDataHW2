import sys
import ast

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1

def updateTotalCount(currentCount, countState):
    if countState is None:
       countState = 0
    return sum(currentCount, countState)


if __name__ == "__main__":
    sc = SparkContext(appName="PythonStreamingRecieverKafkaWordCount")
    ssc = StreamingContext(sc, 6) # 2 second window 
    ssc.checkpoint("/tmp")


    broker, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, broker, "raw-event-streaming-consumer",{topic:1}) 


  #  lines = kvs.map(lambda (key,x): ast.literal_eval(x))
    lines = kvs.map(lambda x: ast.literal_eval(x[1])).map(lambda x : x["af"]).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

    lines.pprint()
  #  counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

   # counts.pprint()
    # update total count for each key
    totalCounts = lines.updateStateByKey(updateTotalCount)

    # print the resulting tuples
    totalCounts.pprint()

    
    ssc.start()
    ssc.awaitTermination()