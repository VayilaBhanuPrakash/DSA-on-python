class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxx = 0
        i = 0
        j = 0
        h = {}
        while j < len(s):
            if s[j] not in h:
                h[s[j]] = 1
            else:
                h[s[j]] += 1
                if h[s[j]] > 2:
                    while h[s[j]] > 2:
                        h[s[i]] -= 1
                        i += 1
            maxx = max(maxx,j-i+1)
            j += 1
        return maxx





        
        