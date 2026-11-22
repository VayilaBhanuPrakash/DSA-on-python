class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for ele in t:
            tMap[ele] = tMap.get(ele, 0) + 1
        
        sMap = {}
        minLen = float('inf')
        res = ""
        count = len(t)
        left = 0

        for right in range(len(s)):

            sMap[s[right]] = sMap.get(s[right], 0) + 1

            if s[right] in tMap and sMap[s[right]] <= tMap[s[right]]:
                count -= 1
            
            while count == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    res = s[left : right + 1]
            
                sMap[s[left]] -= 1

                if s[left] in tMap and sMap[s[left]] < tMap[s[left]]:
                    count += 1

                left += 1
        return res

            

        
        
        