class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dictt={"L":0,"R":0,"_":0}
        for ele in moves:
            dictt[ele]=dictt.get(ele,0)+1
        if dictt["L"]>dictt["R"]:
            return dictt["L"]-dictt["R"]+dictt["_"]
        else:
            return dictt["R"]-dictt["L"]+dictt["_"]


        