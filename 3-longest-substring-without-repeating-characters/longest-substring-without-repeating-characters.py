class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        sett = set()
        j = 0
        max_length = 0
        for i in range(len(st)):
            while st[i] in sett:
                sett.remove(st[j])
                j += 1
            sett.add(st[i])
            max_length = max(max_length,i-j+1)
        return max_length

            

            
        