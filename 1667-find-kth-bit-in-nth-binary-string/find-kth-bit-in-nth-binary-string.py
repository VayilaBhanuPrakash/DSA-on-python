class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n-1):
            inv = ""
            for ele in s:
                if ele =="1":
                    inv = inv + "0"
                else:
                    inv = inv + "1"
            s = s + "1" + inv[::-1]

        return s[k-1]
        