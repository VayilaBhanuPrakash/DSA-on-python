class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        h1 = {chr(i + 97) : 0 for i in range(26)}
        for ele in p:
            h1[ele] += 1

        h2 = {chr(i + 97) : 0 for i in range(26)}
        n = len(p)
        i = 0
        res = []
        for j in range(len(s)):
            if j - i + 1 > n:
                h2[s[i]] -= 1
                i += 1
                
            h2[s[j]] += 1

            if h1 == h2:
                res.append(i)

        return res
        