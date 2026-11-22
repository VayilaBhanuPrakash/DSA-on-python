class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for ele in t:
            tMap[ele] = tMap.get(ele, 0) + 1
        
        sMap = {}
        left = 0
        minLen = float('inf')
        count = len(t)
        ans = ""

        for right in range(len(s)):

            sMap[s[right]] = sMap.get(s[right], 0) + 1

            if s[right] in tMap and sMap[s[right]] <= tMap[s[right]]:
                count -= 1
            
            while count == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    ans = s[left : right + 1]

                sMap[s[left]] -= 1

                if s[left] in tMap and sMap[s[left]] < tMap[s[left]]:
                    count += 1

                left += 1
                
        return ans
        
        
        