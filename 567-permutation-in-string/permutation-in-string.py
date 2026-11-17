class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        for ele in s1:
            if ele in h1:
                h1[ele] += 1
            else:
                h1[ele] = 1
        h2 = {}
        n = len(s1)
        i = 0
        for j in range(len(s2)):
            if j - i + 1 > n:
                h2[s2[i]] -= 1
                if h2[s2[i]] == 0:
                    h2.pop(s2[i])
                i += 1
            if s2[j] not in h2:
                h2[s2[j]] = 1
            else:
                h2[s2[j]] += 1

            if h1 == h2:
                return True

        return False

        