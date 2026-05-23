class Solution:
    def checkString(self, s: str) -> bool:
        h={}
        for ele in s:
            if ele=="a" and "b" in h:
                return False
            else:
                h[ele]=1
        return True
        