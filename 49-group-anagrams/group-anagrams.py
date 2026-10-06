class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for ele in strs:
            s = list(ele)
            s.sort()
            s = "".join(s)
            if s not in h:
                h[s] = [ele]
            else:
                h[s].append(ele)
        res = []
        for values in h.values():
            res.append(values)
        return res        