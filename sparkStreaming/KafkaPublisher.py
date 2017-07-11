from kafka import KafkaClient, SimpleProducer, SimpleConsumer

#Eventualmente aggiungere funzione adaptData per pulire i dati
class KafkaPublisher:
	
	def __init__(self,address,port,topic):
		self.kafka = KafkaClient(str(address)+":"+str(port))
		self.producer = SimpleProducer(self.kafka)
		self.topic=topic



	def pushMessage(self,message):
		self.producer.send_messages(self.topic, message)
		#self.producer = SimpleProducer(self.kafka, async=True)
