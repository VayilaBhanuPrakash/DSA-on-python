class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        h = {"a":0,"b":0,"c":0}
        res = 0
        j = 0
        for i in range(len(s)):
            h[s[i]] += 1
            while h["a"] >= 1 and h["b"] >= 1 and h["c"] >= 1:
                res += (len(s) - i)
                h[s[j]] -= 1
                j += 1
        return res

        