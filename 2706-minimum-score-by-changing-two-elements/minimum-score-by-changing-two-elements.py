class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        first = min(nums)
        last = max(nums)
        nums.remove(first)
        nums.remove(last)
        second = min(nums)
        second_last = max(nums)
        nums.remove(second)
        nums.remove(second_last)
        if not nums:
            third = second_last
            third_last = second
        else:
            third = min(nums)
            third_last = max(nums)
        
        return min(last - third, third_last - first, second_last - second)

        
        