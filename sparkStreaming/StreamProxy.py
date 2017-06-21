from ripe.atlas.cousteau import AtlasStream
from kafka import KafkaClient, SimpleProducer, SimpleConsumer

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)

def on_result_response(*args):
	global kafka
	global producer
	"""
	Function that will be called every time we receive a new result.
	Args is a tuple, so you should use args[0] to access the real message.
	"""
	producer.send_messages("new_topic", str(args[0]))
	producer = SimpleProducer(kafka, async=True)

atlas_stream = AtlasStream()
atlas_stream.connect()
# Measurement results
channel = "atlas_result"
# Bind function we want to run with every result message received
atlas_stream.bind_channel(channel, on_result_response)
# Subscribe to new stream for 1001 measurement results
stream_parameters = {"msm": 1001}
atlas_stream.start_stream(stream_type="result", **stream_parameters)

# Probe's connection status results
channel = "atlas_probestatus"
atlas_stream.bind_channel(channel, on_result_response)
stream_parameters = {"enrichProbes": True}
atlas_stream.start_stream(stream_type="probestatus", **stream_parameters)

# Timeout all subscriptions after 5 secs. Leave seconds empty for no timeout.
# Make sure you have this line after you start *all* your streams
atlas_stream.timeout(seconds=25)
# Shut down everything
atlas_stream.disconnect()