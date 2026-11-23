class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        h ={0 : 1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]

            target = prefix - k
            if target in h:
                res += h[target]
            h[prefix] = h.get(prefix, 0) + 1
        return res
            

            
            
        
        