class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        h = {}
        maxx = 0

        for right in range(len(s)):
            if s[right] in h:
                h[s[right]] += 1
            else:
                h[s[right]] = 1
            
            maxx = max(maxx,h[s[right]])

            if right - left + 1 - maxx > k:
                h[s[left]] -= 1
                left += 1
            res = max(res,right - left + 1)
        return res
                


        