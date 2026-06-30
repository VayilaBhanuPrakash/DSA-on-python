class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        h = {"a":0,"b":0,"c":0}
        n = len(s)
        res = 0
        i = 0
        for j in range(n):
            h[s[j]] += 1
            while h["a"] >= 1 and h["b"] >= 1 and h["c"] >= 1:
                res += (n-j)
                h[s[i]] -= 1
                i += 1
        return res


        