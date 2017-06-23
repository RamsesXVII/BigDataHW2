from ripe.atlas.cousteau import AtlasStream
from KafkaPublisher import KafkaPublisher

class StreamProxy:
	'''Transform the data fetched by Costeau into a dictionary
	that will be used to characterize the periodicity
	TODO:check the dest address'''
	
	def __init__(self,address,port,topic):
		self.kafkaPublisher=KafkaPublisher(address,port,topic)


	def on_result_response(self,*args):
		self.kafkaPublisher.pushMessage(str(args[0]))


	def getStreaming(self,secondsStreaming):

		atlas_stream = AtlasStream()
		atlas_stream.connect()
		# Measurement results
		channel = "atlas_result"
		# Bind function we want to run with every result message received
		atlas_stream.bind_channel(channel, self.on_result_response)
		# Subscribe to new stream for 1001 measurement results
		stream_parameters = {"type": "traceroute"}
		atlas_stream.start_stream(stream_type="result", **stream_parameters)

		# Timeout all subscriptions after 5 secs. Leave seconds empty for no timeout.
		# Make sure you have this line after you start *all* your streams
		atlas_stream.timeout(seconds=secondsStreaming)
		# Shut down everything
		atlas_stream.disconnect()