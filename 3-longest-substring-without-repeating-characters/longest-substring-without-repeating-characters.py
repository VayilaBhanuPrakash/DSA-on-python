class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        s = ""
        maxx = 0
        res = 0
        for letters in st:
            if letters not in s:
                s = s + letters
                maxx += 1
            else:
                while letters in s:
                    s = s[1:]
                    maxx -= 1
                s = s + letters
                maxx += 1
            res = max(res,maxx)
        return res
            
        