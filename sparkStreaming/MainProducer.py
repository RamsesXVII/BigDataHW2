from StreamProxy import StreamProxy


streamProxy=StreamProxy("localhost",9092,"tasks")
streamProxy.getStreaming(3600)  #seconds of streaming
