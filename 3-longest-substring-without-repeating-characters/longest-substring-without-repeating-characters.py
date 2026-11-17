class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        sett = set()
        i = 0
        j = 0
        count = 0
        while j < len(s):
            if s[j] not in sett:
                count += 1
                sett.add(s[j])
            else:
                res = max(res, count)
                while s[j] in sett:
                    sett.remove(s[i])
                    i += 1
                    count -= 1
                sett.add(s[j])
                count += 1
            j += 1
        res = max(res, count)
        return res




        
            

            
        