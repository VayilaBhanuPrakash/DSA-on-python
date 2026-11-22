class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        h = {}
        left = 0

        for right in range(len(s)):
            if s[right] in h:
                left = max(left,h[s[right]] + 1)
            h[s[right]] = right
            res = max(res, right - left + 1)
        return res





        
            

            
        