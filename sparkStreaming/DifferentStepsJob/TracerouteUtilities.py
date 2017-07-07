from sets import Set

class TracerouteUtilities:


	def repliesToString(self,replies):
	        decoded = Set([])
	        for j in range(0, len(replies)):
	            singleReply = replies[j]
	            if "from" in singleReply:
	                decoded.add(singleReply["from"])
	            else: 
	                decoded.add("*")
	        return decoded

	def calculatePath(self,hopsReplies, z):
	    hop = hopsReplies[z]
	    if (len(hop) == 1 and  "*" not in hop):
	        return hop[0]
	    else:
	        if (len(hopsReplies[z-1]) == 1 and len(hopsReplies[z+1]) == 1 and "*" not in hopsReplies[z-1] and "*" not in hopsReplies[z+1]):
	            if len(hop) == 1:
	                intermediateResult = hopsReplies[z-1][0] + "-" + hopsReplies[z+1][0]
	                return intermediateResult
	            else:
	                first = True
	                intermediateResult = ""
	                for w in range(0, len(hop)):
	                    if hop[w] != "*":
	                        if first:
	                            first = False
	                            intermediateResult += hop[w]
	                        else:
	                            intermediateResult += "-" + hop[w]
	                return intermediateResult
	        else:
	            return ""