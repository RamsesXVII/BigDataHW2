from StreamProxy import StreamProxy


streamProxy=StreamProxy("localhost",9092,"task1")
streamProxy.getStreaming(20)  #seconds of streaming
