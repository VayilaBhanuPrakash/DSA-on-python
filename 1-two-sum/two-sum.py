class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in h and h[target - nums[i]] != i:
                return [h[target - nums[i]],i]

            
            