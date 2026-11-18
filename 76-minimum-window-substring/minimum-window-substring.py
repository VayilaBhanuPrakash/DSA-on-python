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
        def valid(h1,h2):
            for ele in h1:
                if ele not in h2 or h2[ele] < h1[ele]:
                    return False
            return True
        while j < len(s):
            if s[j] in h1:
                if s[j] not in h2:
                    h2[s[j]] = 1
                else:
                    h2[s[j]] += 1

            while i < len(s) and valid(h1,h2):
                if len(s[i : j + 1]) < minn:
                    minn = len(s[i : j + 1])
                    res = s[i : j + 1]
                if s[i] in h2:
                    h2[s[i]] -= 1
                i += 1 
            j += 1
        return res
        