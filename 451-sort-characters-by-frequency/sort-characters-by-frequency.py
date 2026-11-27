class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        for ele in s:
            h[ele] = h.get(ele, 0) + 1
        
        h = dict(sorted(h.items(), key = lambda x : x[1], reverse = True))

        res = []
        for key in h:
            for i in range(h[key]):
                res.append(key)
        
        return "".join(res)
        