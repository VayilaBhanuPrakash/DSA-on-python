class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        h = {}
        left = 0
        max_freq = 0

        for right in range(len (s)):
            if s[right] in h:
                h[s[right]] += 1
            else:
                h[s[right]] = 1
            
            max_freq = max(max_freq,h[s[right]])

            if (right - left + 1) - max_freq > k:
                h[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res
        