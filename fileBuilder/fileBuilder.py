import requests

with open("ipv4Ids") as f: 
    content = f.readlines()

ids = [x.strip() for x in content] 

out_file = open("../resources/recordDownload.json","w") #
out_fileIdsMeasurement = open("../resources/IdsList","w") #dovrebbe tenere  conto di quelli che effettivamente hannofatto un download


for id in ids:
	print(id)
	data = requests.get("https://atlas.ripe.net/api/v2/measurements/"+id+"/results?start=1498838400&stop=1498849200&format=txt")

	if(data):
		out_fileIdsMeasurement.write(id+"\n")
		out_file.write(str(data.text)+"\n")
out_file.close()

