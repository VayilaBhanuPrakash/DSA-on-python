class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        n = len(s)
        sett = set()
        for right in range(n):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            res = max(res, right - left + 1)
        return res        




        
            

            
        