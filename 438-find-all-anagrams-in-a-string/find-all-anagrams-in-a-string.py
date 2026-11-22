class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(s) < len(p):
            return res

        pmap = {}
        for ele in p:
            pmap[ele] = pmap.get(ele, 0) + 1

        left = 0
        count = len(p)

        for right in range(len(s)):
            if s[right] not in pmap:
                pmap[s[right]] = -1
            if pmap[s[right]] > 0:
                count -= 1
            pmap[s[right]] -= 1

            if right - left + 1 > len(p):
                if pmap[s[left]] >= 0:
                    count += 1
                pmap[s[left]] += 1
                left += 1
            if count == 0:
                res.append(left)
        return res


        
        