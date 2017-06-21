from kafka import KafkaClient, SimpleProducer, SimpleConsumer
kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
producer.send_messages("new topic", "sono entrato")
#[ProduceResponsePayload(topic=u'new_topic', partition=0, error=0, offset=0)]
producer.send_messages("new topic", "bella", "zi")
#[ProduceResponsePayload(topic=u'new_topic', partition=0, error=0, offset=1)]
producer = SimpleProducer(kafka, async=True)
