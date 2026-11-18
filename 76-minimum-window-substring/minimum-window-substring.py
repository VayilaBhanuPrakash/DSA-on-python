class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h1 = {}
        for ele in t:
            if ele in h1:
                h1[ele] += 1
            else:
                h1[ele] = 1
        
        h2 = {}
        i =  0
        j = 0
        res = ""
        minn = len(s) + 1
        count = 0
        count2 = len(h1)
        while j < len(s):
            if s[j] in h1:
                if s[j] not in h2:
                    h2[s[j]] = 1
                else:
                    h2[s[j]] += 1
                if h1[s[j]] == h2[s[j]]:
                    count += 1
            while i < len(s) and count == count2:
                if j - i + 1 < minn:
                    minn = j - i + 1
                    res = s[i : j + 1]
                if s[i] not in h2:
                    i += 1
                else:
                    h2[s[i]] -= 1
                    if h2[s[i]] < h1[s[i]]:
                        count -= 1
                    i += 1
            j += 1


            
        return res
        