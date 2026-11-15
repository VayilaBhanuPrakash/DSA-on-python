class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        h = {"0" : "1","1" : "0"}
        for i in range(n-1):
            inv = ""
            for ele in s:
                inv = inv + h[ele]
            s = s + "1" + inv[::-1]

        return s[k-1]
        