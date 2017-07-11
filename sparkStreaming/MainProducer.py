from StreamProxy import StreamProxy


streamProxy=StreamProxy("localhost",9092,"tasks")
streamProxy.getStreaming(60)  #seconds of streaming
