# Big Data Homework 2

[![N|Solid](https://www-static.ripe.net/static/rnd-ui/atlas/media/anchors/RIPE_NCC_Logo2015-256_q3prZmW.png)](https://atlas.ripe.net/)
### Dati
Data used in batch analysis are anchoring measurements traceroutes running on the 13th of June in 2017. 
Traceroute records are obtained by a script that downloads  measurements specified in input file, adding new records on tail of output file.
Requests are structured as  follows:

> https://atlas.ripe.net/api/v2/measurements/"+id+"/results?start=1497312000&stop=1497398399&format=txt

### Task 1
Distribution of hop counts.

### Task 2
Detection of anomalies in rtt

### Spark Streaming
  - SEGUIRE LA GUIDA NUMERO 1 PER MODIFICARE LE IMPOSTAZIONI IN .PROPERTIES
  - AVVIARE ZOOKEPER 
  
```sh
$ bin/zookeeper-server-start.sh config/zookeeper.properties 
```
  - AVVIARE KAFKA
```sh
$ bin/kafka-server-start.sh config/server.properties 
```
  - AVVIARE IL CONSUMER
```sh
$  ./spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.1 /home/iori/Desktop/consumer.py localhost:2181 new_topic 
```
  - POSTARE UN MESSAGGIO DA RIGA DI COMANDO
```sh
$   echo "ciao bello" | ./kafka-console-producer.sh --broker-list localhost:9092 --topic new_topic
```

### Tutorial

https://kafka.apache.org/quickstart
https://medium.com/@kass09/spark-streaming-kafka-in-python-a-test-on-local-machine-edd47814746 (l'ultima parte è importante e non l'ho letta)



### ToDo
  - Extend the input on Built-In and UDM. 
  - Check that ids in idFile.txt correspond to measurement running (grep is enough?)
  - Magic

