class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {chr(i + 97) : 0 for i in range(26)}
        for ele in s1:
            h1[ele] += 1

        h2 = {chr(i + 97) : 0 for i in range(26)}
        n = len(s1)
        i = 0
        for j in range(len(s2)):
            if j - i + 1 > n:
                h2[s2[i]] -= 1
                i += 1
                
            h2[s2[j]] += 1

            if h1 == h2:
                return True

        return False
        