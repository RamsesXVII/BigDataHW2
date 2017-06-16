import requests

with open("idsList(ipv4 o ipv6)") as f: 
    content = f.readlines()

ids = [x.strip() for x in content] 

out_file = open("recordDownload","w") #
out_fileIdsMeasurement = open("IdsList","w")#dovrebbe tenere  conto di quelli che effettivamente hannofatto un download


for id in ids:
	print(id)
	data = requests.get("https://atlas.ripe.net/api/v2/measurements/"+id+"/results?start=1497312000&stop=1497398399&format=txt")

	if(data):
		out_fileIdsMeasurement.write(id+"\n")
		out_file.write(str(data.text)+"\n")
out_file.close()



