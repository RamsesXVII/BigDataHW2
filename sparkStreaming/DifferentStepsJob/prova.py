import ast
from sets import Set

input1 = "{'af':4,'dst_addr':'163.237.247.18','dst_name':'163.237.247.18','endtime':1497329951,'from':'80.241.3.66','fw':4770,'group_id':8627598,'lts':41,'msm_id':8627598,'msm_name':'Traceroute','paris_id':1,'prb_id':6086,'proto':'ICMP','result':[{'hop':1,'result':[{'from':'80.241.3.1','rtt':0.663,'size':28,'ttl':255},{'from':'80.241.3.1','rtt':0.543,'size':28,'ttl':255},{'from':'80.241.3.1','rtt':0.483,'size':28,'ttl':255}]},{'hop':2,'result':[{'from':'88.204.208.1','rtt':0.685,'size':28,'ttl':253},{'from':'88.204.208.1','rtt':22.569,'size':28,'ttl':253},{'from':'88.204.208.1','rtt':51.119,'size':28,'ttl':253}]},{'hop':3,'result':[{'from':'92.47.151.241','icmpext':{'obj':[{'class':1,'mpls':[{'exp':1,'label':712658,'s':1,'ttl':1}],'type':1}],'rfc4884':0,'version':2},'rtt':25.011,'size':140,'ttl':246},{'from':'92.47.151.241','icmpext':{'obj':[{'class':1,'mpls':[{'exp':1,'label':712658,'s':1,'ttl':1}],'type':1}],'rfc4884':0,'version':2},'rtt':25.094,'size':140,'ttl':246},{'from':'92.47.151.241','icmpext':{'obj':[{'class':1,'mpls':[{'exp':1,'label':712658,'s':1,'ttl':1}],'type':1}],'rfc4884':0,'version':2},'rtt':24.969,'size':140,'ttl':246}]},{'hop':4,'result':[{'from':'95.59.172.15','rtt':29.302,'size':28,'ttl':248},{'from':'95.59.172.15','rtt':35.722,'size':28,'ttl':248},{'from':'95.59.172.15','rtt':24.85,'size':28,'ttl':248}]},{'hop':5,'result':[{'from':'217.150.44.146','rtt':40.734,'size':68,'ttl':247},{'from':'217.150.44.146','rtt':40.594,'size':68,'ttl':247},{'from':'217.150.44.146','rtt':40.638,'size':68,'ttl':247}]},{'hop':6,'result':[{'from':'212.162.24.170','icmpext':{'obj':[{'class':0,'type':0}],'rfc4884':1,'version':0},'rtt':107.207,'size':140,'ttl':242},{'from':'212.162.24.170','icmpext':{'obj':[{'class':0,'type':0}],'rfc4884':1,'version':0},'rtt':108.404,'size':140,'ttl':242},{'from':'212.162.24.170','icmpext':{'obj':[{'class':0,'type':0}],'rfc4884':1,'version':0},'rtt':107.381,'size':140,'ttl':242}]},{'hop':7,'result':[{'from':'212.162.24.169','rtt':108.966,'size':28,'ttl':242},{'from':'212.162.24.169','rtt':109.093,'size':28,'ttl':242},{'from':'212.162.24.169','rtt':108.832,'size':28,'ttl':242}]},{'hop':8,'result':[{'x':'*'},{'x':'*'},{'x':'*'}]},{'hop':9,'result':[{'from':'130.117.14.173','rtt':112.825,'size':68,'ttl':244},{'from':'130.117.14.173','rtt':113.215,'size':68,'ttl':244},{'from':'130.117.14.173','rtt':113.073,'size':68,'ttl':244}]},{'hop':10,'result':[{'from':'154.54.37.29','rtt':109.5,'size':68,'ttl':243},{'from':'154.54.37.29','rtt':109.718,'size':68,'ttl':243},{'from':'154.54.37.29','rtt':109.49,'size':68,'ttl':243}]},{'hop':11,'result':[{'from':'130.117.0.141','rtt':126.054,'size':68,'ttl':242},{'from':'130.117.0.141','rtt':125.493,'size':68,'ttl':242},{'from':'130.117.0.141','rtt':125.384,'size':68,'ttl':242}]},{'hop':12,'result':[{'from':'154.54.58.69','rtt':137.008,'size':68,'ttl':241},{'from':'83.169.204.78','rtt':88.42,'size':28,'ttl':243},{'from':'130.117.50.121','rtt':105.433,'size':68,'ttl':243}]},{'hop':13,'result':[{'from':'154.54.63.1','rtt':122.576,'size':68,'ttl':242},{'from':'154.54.63.1','rtt':122.314,'size':68,'ttl':242},{'from':'154.54.63.1','rtt':122.528,'size':68,'ttl':242}]},{'hop':14,'result':[{'from':'154.54.38.205','rtt':127.388,'size':68,'ttl':242},{'from':'154.54.38.205','rtt':127.253,'size':68,'ttl':242},{'from':'154.54.38.205','rtt':126.588,'size':68,'ttl':242}]},{'hop':15,'result':[{'from':'154.54.77.246','rtt':140.089,'size':68,'ttl':241},{'from':'154.54.77.246','rtt':140.24,'size':68,'ttl':241},{'from':'154.54.77.246','rtt':140.113,'size':68,'ttl':241}]},{'hop':16,'result':[{'from':'154.54.44.162','rtt':198.564,'size':68,'ttl':240},{'from':'154.54.44.162','rtt':198.308,'size':68,'ttl':240},{'from':'154.54.44.162','rtt':198.343,'size':68,'ttl':240}]},{'hop':17,'result':[{'from':'154.54.41.205','rtt':212.455,'size':68,'ttl':239},{'from':'154.54.41.205','rtt':212.311,'size':68,'ttl':239},{'from':'154.54.41.205','rtt':212.277,'size':68,'ttl':239}]},{'hop':18,'result':[{'from':'154.54.31.225','rtt':220.666,'size':68,'ttl':238},{'from':'163.237.254.18','rtt':205.593,'size':28,'ttl':241},{'from':'163.237.254.18','rtt':211.035,'size':28,'ttl':241}]},{'hop':19,'result':[{'from':'163.237.247.18','rtt':200.137,'size':48,'ttl':51},{'from':'163.237.247.18','rtt':200.182,'size':48,'ttl':51},{'from':'163.237.247.18','rtt':200.139,'size':48,'ttl':51}]}],'size':48,'src_addr':'80.241.3.66','timestamp':1497329932,'type':'traceroute'}"


trace = ast.literal_eval(input1)
result = ""
stringhe = []
source = trace["from"]
destination = trace["dst_addr"]
hopList = trace["result"]
finalStep = hopList[len(hopList)-1]
if "hop" in finalStep:
    finalHop = hopList[len(hopList)-1]["hop"]
    if finalHop == 255:
        print("error 1")
    else:
        for i in range(0,len(hopList)):
            replies = hopList[i]["result"]
            coded = Set([])
            for j in range(0, len(replies)):
                singleReply = replies[j]
                if "from" in singleReply:
                    coded.add(singleReply["from"])
                else: 
                    coded.add("*")
            stringhe.insert(i, sorted(coded))

        if len(stringhe[0]) == 1:

            for z in range(0, len(stringhe)-1):
                hop = stringhe[z]
                if (len(hop) == 1 and hop[0] != "*"):
                    result += hop[0] + ","
                else:
                    if (len(stringhe[z-1]) == 1 and len(stringhe[z+1]) == 1):
                        if len(hop) == 1:
                            result += stringhe[z-1][0] + "-" + stringhe[z+1][0]
                        else:
                            first = True
                            for w in range(0, len(hop)):
                                if hop[w] != "*":
                                    if first:
                                        first = False
                                        result += hop[w]
                                    else:
                                        result += "-" + hop[w]
                        result += ","
                    else:
                        print("error 3")
    print result
else:
    print "error 2"