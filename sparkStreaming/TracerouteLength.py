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

def getHop(trace):
    hopList = trace["result"]
    lista = hopList[len(hopList)-1]
    if "hop" in lista:
        finalHop = hopList[len(hopList)-1]["hop"]
        return (finalHop, 1)
    print(lista)
    return ()



if __name__ == "__main__":
    sc = SparkContext(appName="TracerouteLength")
    ssc = StreamingContext(sc, 10) # 10 second window 
    ssc.checkpoint("/tmp")


    broker, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, broker, "TracerouteLengthTask",{topic:1}) 


    lines = kvs.map(lambda x: ast.literal_eval(x[1])).map(lambda trace: getHop(trace)).reduceByKey(lambda a, b: a+b)

    lines.pprint()
  #  counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

   # counts.pprint()
    # update total count for each key
    totalCounts = lines.updateStateByKey(updateTotalCount)

    # print the resulting tuples
    totalCounts.pprint()

    
    ssc.start()
    ssc.awaitTermination()
