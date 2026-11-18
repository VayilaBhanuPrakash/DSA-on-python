class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h1 = {}
        for ele in t:
            h1[ele] = h1.get(ele, 0) + 1
        
        h2 = {}
        i =  0
        j = 0
        res = ""
        minn = len(s) + 1
        n = len(s)
        count1 = len(h1)
        count2 = 0
        while j < n:
            if s[j] in h1:
                h2[s[j]] = h2.get(s[j], 0) + 1
                if h1[s[j]] == h2[s[j]]:
                    count2 += 1
            while i < n and count1 == count2:
                if j - i + 1 < minn:
                    minn = j - i + 1
                    res = s[i : j + 1]
                if s[i] not in h2:
                    i += 1
                else:
                    h2[s[i]] -= 1
                    if h2[s[i]] < h1[s[i]]:
                        count2 -= 1
                    i += 1
            j += 1


            
        return res
        