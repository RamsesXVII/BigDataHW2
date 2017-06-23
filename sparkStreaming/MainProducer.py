from StreamProxy import StreamProxy


streamProxy=StreamProxy("localhost",9092,"new_topic")
streamProxy.getStreaming(2)  #seconds of streaming