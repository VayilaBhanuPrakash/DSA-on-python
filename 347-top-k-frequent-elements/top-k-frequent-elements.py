class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for ele in nums:
            if ele in h:
                h[ele] += 1
            else:
                h[ele] =1
        res = []
        h = dict(sorted(h.items(), key = lambda x:x[1],reverse=True))
        i = 0 
        for keys in h:
            if i < k:
                res.append(keys)
                i+=1
            else:
                break
        return res

        
        