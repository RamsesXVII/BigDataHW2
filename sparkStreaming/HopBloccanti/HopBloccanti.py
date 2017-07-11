import sys
import ast
from sets import Set
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def updateTotalCount(currentCount, countState):
    
    if len(currentCount) != 0:
        totCurrent = currentCount[0][0]
        uniqCurrent = currentCount[0][1]
    else:
        totCurrent = 0
        uniqCurrent = 0

    if countState is None:
        totState = 0
        uniqState = 0
    else:
        totState = countState[0]
        uniqState = countState[1]

    return totCurrent + totState , uniqCurrent + uniqState


def checkHop(trace):
    error = ("x", 1)

    if "dst_addr" not in trace:
        return error

    hopList = trace["result"]

    probeId = trace["prb_id"]
    measurementId = trace["msm_id"]
    tracerouteKey = str(probeId) + "," + str(measurementId)

    finalStep = hopList[len(hopList)-1]

    if "hop" not in finalStep:
        return error

    if finalStep["hop"]!= 255: 
        return error

    for i in range(len(hopList)-2, -1, -1):
        singleHop = hopList[i]

        if "result" not in singleHop:
            return error

        replies = singleHop["result"]

        for y in range(0, len(replies)):
            reply = replies[y]

            if "from" in reply:
                return (reply["from"], tracerouteKey)
    return error

if __name__ == "__main__":

    sc = SparkContext(appName="HopBloccanti")
    ssc = StreamingContext(sc, 20) # 10 second window 
    ssc.checkpoint("/tmp")

    broker, topic, path = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, broker, "HopBloccanti",{topic:1}) 


    lines = kvs.map(lambda x: ast.literal_eval(x[1])).map(lambda trace: checkHop(trace)).filter(lambda (x,y): x != "x").groupByKey().map(lambda (x,y): (x, (len(y),len(set(y)))))
    
    # update total count for each key
    totalCounts = lines.updateStateByKey(updateTotalCount)

    # print the resulting tuples
    totalCounts.pprint()
    totalCounts.saveAsTextFiles("file://" + path)

    ssc.start()
    ssc.awaitTermination()