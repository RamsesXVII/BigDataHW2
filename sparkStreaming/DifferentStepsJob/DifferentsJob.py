import sys
import ast
from sets import Set
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from TracerouteUtilities import TracerouteUtilities

utility = TracerouteUtilities()

def updateTotalCount(currentCount, countState):
    if countState is None:
       countState = 0
    return sum(currentCount, countState)

def checkSteps(trace):
    global utility
    error = ("x",1)
    if "dst_addr" not in trace:
        return error

    result = ""
    source = trace["from"]
    destination = trace["dst_addr"]
    key = source + destination
    hopList = trace["result"]
    finalStep = hopList[len(hopList)-1]

    if "hop" not in finalStep:
        return error

    finalHop = hopList[len(hopList)-1]["hop"]
    if finalHop == 255:
        return error

    hopsReplies = []
    for i in range(0,len(hopList)):

        if "result" not in hopList[i]:
            return ("x",1)

        replies = hopList[i]["result"]
        hopsReplies.insert(i, sorted(utility.repliesToString(replies)))

    if len(hopsReplies[0]) == 1:
        for z in range(0, len(hopsReplies)-1):                
            hopResult = utility.calculatePath(hopsReplies, z)

            if len(hopResult) == 0:
                return ("x",1)

            result += hopResult + ","
    else:
        return error

    finalReplies = hopsReplies[len(hopsReplies)-1]
    for y in range(0, len(finalReplies)):
        if finalReplies[y] != "*":
            result += finalReplies[y]
            return (key,result)
    return error

if __name__ == "__main__":
    sc = SparkContext(appName="TracerouteLength")
    ssc = StreamingContext(sc, 10) # 10 second window 
    ssc.checkpoint("/tmp")

    broker, topic, path = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, broker, "TracerouteLengthTask",{topic:1}) 


    lines = kvs.map(lambda x: ast.literal_eval(x[1])).map(lambda trace: checkSteps(trace)).filter(lambda (x,y): x != "x").groupByKey().map(lambda (x,y): (len(set(y)),1)).reduceByKey(lambda a,b: a+b)
    
    # update total count for each key
    totalCounts = lines.updateStateByKey(updateTotalCount)

    # print the resulting tuples
    totalCounts.pprint()
    totalCounts.saveAsTextFiles("file://" + path)

    ssc.start()
    ssc.awaitTermination()