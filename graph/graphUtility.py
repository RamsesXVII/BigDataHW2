import ast
import time 
from neo4j.v1 import GraphDatabase, basic_auth
'''Genera due file csv, il primo, "ipAddressesGlobal.csv" è del tipo id, indirizzo ip e contiene 
la lista degli indirizzi ip univoci incontrati, il secondo "ipPairsGlobal.csv" è del tipo ipPrev,ipNext 
e coniente la lista degli archi univoci incontrati. L'input richiesto è un file che per ogni riga contiene un
record ottenuto tramite cousteau. NB: sono esclusi dalle operazioni gli asterischi e gli hop che compaiono con diversi 
ip associati.'''


def isNotPrivate(ip):
    if ip[:3]=="10.":
        return False
    if ip[:8]=="192.168.":
        return False
    if ip[:4]=="172.":
        substring=ip[4:]
        substring=int(substring[:(substring.index('.'))])
        if substring>15 and substring<32:
            return False
    return True



def getIDtoThresholdedTraceroute(pathToFile):

    with open(pathToFile) as inputStreaming:
        for record in inputStreaming: #e una sola riga
            idToTraceroute=ast.literal_eval(record)

    return idToTraceroute

def getStringOfCleanedTraceroute(traceroute): #i traceroute sono nella forma hop1,hop
    splittedTrace


nodeCounter=0

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "password"))
session = driver.session()

idToTraceroute=getIDtoThresholdedTraceroute("idToTracerouteGlobal.txt")

print("record to insert: "+str(len(idToTraceroute)))

pairsCounter=0
lineCounter=0

initialTime=time.time()
pairsSet=set()
IPsAddress=set()

for key in idToTraceroute:

    traceroute=idToTraceroute[key]
    tracerouteSplitted= traceroute.split(',')
    i=len(tracerouteSplitted)

    lineCounter+=1
    if lineCounter%100==0:
        print lineCounter

    try:
        prev=tracerouteSplitted[0]
        if isNotPrivate(prev):
            if "*" not in prev and "-" not in prev:
                nodeCounter+=1
                IPsAddress.add(prev)

        for counter in range(1,i):
            next = tracerouteSplitted[counter]
            if isNotPrivate(next):
                if "*" not in next and "-" not in next:
                    nodeCounter+=1
                    IPsAddress.add(next)
            if isNotPrivate(prev) and isNotPrivate(next):
                if "*" not in prev and "*" not in next and "-" not in prev and "-" not in next:
                    pairsSet.add(prev+","+next)
            prev=next

    except Exception:
         print "error"


print("numero nodi")
print(len(IPsAddress))
print("numero relazioni")

print(len(pairsSet))
#print(pairsSet)
'''
counter=0
#persisto i singoli nodi
for ip in IPsAddress:
    counter+=1
    if counter%10000==0:
        print counter
    session.run("CREATE (a:ipNode {ipAddress: {ipAddress}})", {"ipAddress": str(ip)})

counter=0
for pair in pairsSet:
    counter+=1
    if counter%10000==0:
        print counter

    pairSplitted=pair.split("-")
    session.run("match (a:ipNode {ipAddress: '"+pairSplitted[0]+"'}),(b:ipNode {ipAddress: '"+pairSplitted[1]+"'}) with a,b create unique (a)-[:precede]->(b)")

'''
out_file=open("ipAddressesGlobal.csv","w")
out_file.write("id,address \n")
counter=0
#persisto i singoli nodi
for ip in IPsAddress:
    counter+=1
    out_file.write(str(counter)+","+ip+"\n")

out_file.close()

out_file=open("ipPairsGlobal.csv","w")
out_file.write("ipPrev,ipNext \n")
counter=0
#persisto i singoli nodi
for ip in pairsSet:
    counter+=1
    out_file.write(ip+"\n")

out_file.close()
print ("numero di nodi attraversati "+ str(nodeCounter))
session.close()
