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
    
def getIp(trace):
    hopList = trace["result"]
    resultList = []
    ipCount = 0
    for i in range(0,len(hopList)):
        singleHop = hopList[i]
        if "result" in singleHop:
            icmpList = singleHop["result"]
            for y in range(0,len(icmpList)):
                if "from" in icmpList[y]:
                    ipCount += 1
                    resultList.append((icmpList[y]["from"], 1))
    resultList.append(("total", ipCount))
    return resultList


if __name__ == "__main__":
    sc = SparkContext(appName="TracerouteLength")
    ssc = StreamingContext(sc, 10) # 10 second window 
    ssc.checkpoint("/tmp")


    broker, topic, path = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, broker, "TracerouteLengthTask",{topic:1}) 


    lines = kvs.map(lambda x: ast.literal_eval(x[1])).filter(lambda x: x["af"] == 6).flatMap(lambda trace: getIp(trace)).reduceByKey(lambda a,b: a+b)
    
    # update total count for each key
    totalCounts = lines.updateStateByKey(updateTotalCount)

    # print the resulting tuples
    totalCounts.pprint()
    totalCounts.saveAsTextFiles("file://" + path)

    ssc.start()
    ssc.awaitTermination()