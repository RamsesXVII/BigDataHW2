from neo4j.v1 import GraphDatabase, basic_auth
import requests, json

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "password"))
session = driver.session()


queryToCount="match (n) return n.ipAddress as ip"
results = session.run(queryToCount)

ipAdds=set()

for record in results:
	print(record)
	ipAdds.add(record["ip"])

asToCount=dict()

for ipAddress in ipAdds:
	url="https://stat.ripe.net/data/whois/data.json?resource="+str(ipAddress)
	data = requests.get(url)
	if data:
		data = data.json()

		try:
			if data["data"]["irr_records"][0][2]["value"] not in asToCount:
				asToCount[str(data["data"]["irr_records"][0][2]["value"])+"-"+ipAddress]=1
			else:
				asToCount[data["data"]["irr_records"][0][2]["value"]+"-"+ipAddress]+=1
		except:
			print("***********")
			print(ipAddress)
			print("***********")

		#print(data["data"]["irr_records"][0][2]["value"])
counter=0

for c in asToCount:
	counter+=asToCount[c]

print(asToCount)
#	match (n:ipNode)-[r:precede]-(m:ipNode) with n, count(r) as DegreeScore where DegreeScore=1 delete detach (n) return count(n)

#match (n:ipNode)-[r:precede]-(m:ipNode) with n, count(r) as DegreeScore where DegreeScore>1 detach delete (n)

