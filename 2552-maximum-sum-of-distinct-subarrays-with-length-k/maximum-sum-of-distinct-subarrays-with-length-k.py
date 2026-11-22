class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        h = {}
        n = len(nums)
        summ = 0
        for i in range(k):
            summ += nums[i]
            h[nums[i]] = h.get(nums[i], 0) + 1
        
        maxx = 0
        if len(h) == k:
            maxx = summ
        
        left = 0
        right = k
        while left < n - k:
            summ -= nums[left]
            summ += nums[right]
            h[nums[left]] -= 1
            if h[nums[left]] == 0:
                h.pop(nums[left])
            h[nums[right]] = h.get(nums[right], 0) + 1
            if len(h) == k:
                maxx = max(maxx,summ)
            left += 1
            right += 1
        return maxx
            
            

        