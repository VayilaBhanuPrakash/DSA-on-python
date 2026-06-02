class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor=0
        for ele in s:
            xor=xor^ord(ele)
        for ele in t:
            xor=xor^ord(ele)
        return chr(xor)
        