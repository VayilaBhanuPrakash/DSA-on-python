class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        n=len(s)
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for i in range(n):
            if d[s[i]]==1:
                return i
        return -1
        