import ast
'''Il file in input deve avere per ciascuna riga un record ottenuto tramite Cousteau. L'output è un dizionario che ha come chiave 
probe-misurazione e come valore l'ultimo traceroute disponibile nella finestra osservata.'''

idToTraceroute=dict()
idToTracerouteAsteriskAnomalies=dict()
idToTracerouteDifferentIP=dict()
idToTracerouteErrorAnomalies=dict()
idToTracerouteGlobal=dict()

lineCounter=0
with open("IPv4hours.txt") as inputStreaming:
	for record in inputStreaming:
		lineCounter+=1
		if lineCounter%1000==0:
			print lineCounter

		onlyAsteriskAtHop=False
		differtIPAtHop=False
		errorHop=False

		traceroute=""
		parsedRecord=ast.literal_eval(record)

		if "result" and "prb_id" and "timestamp" and "msm_id" in parsedRecord: #controllo se il recordo e' valido se non lo e' viene ignorato direttamente

			prb_id=parsedRecord["prb_id"]
			timestamp=parsedRecord["timestamp"]
			msm_id=parsedRecord["msm_id"]
			results=parsedRecord["result"]

			hopCounter=0

			for hop in results:

				if "error" not in hop:   
					differtIP=set()
					icmpSize=len(hop["result"])

					for counter in range(0,icmpSize):

						if "from" in hop["result"][counter]: #vengono aggiunti gli indirizzi ip presenti in un hop ad un set, gli asterischi non sono contati
							differtIP.add(hop["result"][counter]["from"])
							currentIP=hop["result"][counter]["from"]


					if(len(differtIP)) == 0: 
						onlyAsteriskAtHop=True
						traceroute+=("*,")

					elif(len(differtIP))>1:  
						differtIPAtHop=True

						for ipAddress in differtIP:
							traceroute+=(str(ipAddress)+"-")

						traceroute=traceroute[:-1]

					else:
						traceroute+=str(currentIP)+","
				else:
					traceroute+="na,"
					errorHop=True

				hopCounter+=1

		idToTracerouteGlobal[str(prb_id)+"-"+str(msm_id)]=traceroute[:-1]

		if onlyAsteriskAtHop:
			idToTracerouteAsteriskAnomalies[str(prb_id)+"-"+str(msm_id)+"-"+str(timestamp)]=traceroute[:-1]

		elif errorHop:
			idToTracerouteErrorAnomalies[str(prb_id)+"-"+str(msm_id)+"-"+str(timestamp)]=traceroute[:-1]


		elif differtIPAtHop:
			idToTracerouteDifferentIP[str(prb_id)+"-"+str(msm_id)+"-"+str(timestamp)]=traceroute[:-1]
		else:
			idToTraceroute[str(prb_id)+"-"+str(msm_id)+"-"+str(timestamp)]=traceroute[:-1]

'''
out_file=open("idToTracecerouteNoAnomalies.txt","w")
out_file.write(str(idToTraceroute))
out_file.close()


out_file=open("idToTracerouteAsteriskAnomalies.txt","w")
out_file.write(str(idToTracerouteAsteriskAnomalies))
out_file.close()

out_file=open("idToTracerouteDifferentIPAnomalies.txt","w")
out_file.write(str(idToTracerouteDifferentIP))
out_file.close()

out_file=open("idToTracerouteHopError.txt","w")
out_file.write(str(idToTracerouteDifferentIP))
out_file.close()
'''
out_file=open("idToTracerouteGlobal.txt","w")
out_file.write(str(idToTracerouteGlobal))
out_file.close()
