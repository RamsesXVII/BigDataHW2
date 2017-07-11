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

    def checkSteps(self,trace):
        error = ("x",1)
        if "dst_addr" not in trace:
            return error

        result = ""
        source = trace["from"]
        destination = trace["dst_addr"]
        key = source + destination
        hopList = trace["result"]
        finalStep = hopList[len(hopList)-1]

        if "hop" not in finalStep:
            return error

        finalHop = hopList[len(hopList)-1]["hop"]
        if finalHop == 255:
            return error

        hopsReplies = []
        for i in range(0,len(hopList)):

            if "result" not in hopList[i]:
                return ("x",1)

            replies = hopList[i]["result"]
            hopsReplies.insert(i, sorted(self.repliesToString(replies)))

        if len(hopsReplies[0]) == 1:
            for z in range(0, len(hopsReplies)-1):                
                hopResult = self.calculatePath(hopsReplies, z)

                if len(hopResult) == 0:
                    return ("x",1)

                result += hopResult + ","
        else:
            return error

        finalReplies = hopsReplies[len(hopsReplies)-1]
        for y in range(0, len(finalReplies)):
            if finalReplies[y] != "*":
                result += finalReplies[y]
                return (key,result)
        return error
