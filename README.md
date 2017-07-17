# Big Data Homework 2

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
  - Seguire la guida numero 1 dei tutorial per modificare le proprietà
  - Avviare Zookeeper
  
```sh
$ bin/zookeeper-server-start.sh config/zookeeper.properties 
```
  - Avviare Kafka
```sh
$ bin/kafka-server-start.sh config/server.properties 
```
  - Avviare il consumer
```sh
$  ./spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.1 /home/iori/Desktop/consumer.py localhost:2181 new_topic 
```
  - Postare un messaggio da riga di comando
```sh
$   echo "ciao bello" | ./kafka-console-producer.sh --broker-list localhost:9092 --topic new_topic
```
 - Avviare un job
```sh
$  ./spark-submit --py-files /other/class/path --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.1 /path/to/job.py localhost:2181 tasks /path/to/output/result 
```

### Tutorial

https://kafka.apache.org/quickstart
https://medium.com/@kass09/spark-streaming-kafka-in-python-a-test-on-local-machine-edd47814746 (l'ultima parte è importante e non l'ho letta)



