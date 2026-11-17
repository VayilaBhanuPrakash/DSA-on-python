class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            sett = set()
            count = 0
            for j in range(i,len(s)):
                if s[j] not in sett:
                    sett.add(s[j])
                    count += 1
                else:
                    res = max(res, count)
                    break
            res = max(res, count)
        return res


        
            

            
        