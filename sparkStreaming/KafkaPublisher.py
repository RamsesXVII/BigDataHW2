from kafka import KafkaClient, SimpleProducer, SimpleConsumer


class KafkaPublisher:
	
	def __init__(self,address,port,topic):
		self.kafka = KafkaClient(str(address)+":"+str(port))
		self.producer = SimpleProducer(self.kafka)
		self.topic=topic



	def pushMessage(self,message):
		"""
		Function that will be called every time we receive a new result.
		Args is a tuple, so you should use args[0] to access the real message.
		"""
		self.producer.send_messages(self.topic, message)
		self.producer = SimpleProducer(self.kafka, async=True)
