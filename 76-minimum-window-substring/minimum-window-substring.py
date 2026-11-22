class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h = {}
        for ele in t:
            h[ele] = h.get(ele, 0) + 1
        
        minLen = float('inf')
        res = ""
        count = len(t)
        left = 0

        for right in range(len(s)):
            if s[right] in h:
                if h[s[right]] > 0:
                    count -= 1
                h[s[right]] -= 1
            
            while count == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    res = s[left : right + 1]
                
                if s[left] in h:
                    h[s[left]] += 1
                    if h[s[left]] > 0:
                        count += 1
                
                left += 1
        return res


            

            

        
        
        