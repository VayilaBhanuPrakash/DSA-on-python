class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        n=len(s)
        for i in t:
            if j<n and i==s[j]:
                j+=1
        return j==n

        