class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        """n = len(nums)
        nums.sort()
        return min((nums[n - 2] - nums[1]), (nums[n - 3] - nums[0]), (nums[n - 1] - nums[2]))"""
        if len(nums) == 3:
            return 0
        first = second = third = float('inf')   
        last = second_last = third_last = float('-inf')  
        for ele in nums:
            if ele < first:
                first, second, third = ele, first, second
            elif ele < second: 
                second, third = ele, second
            elif ele < third: 
                third = ele
            if ele > last:
                last, second_last, third_last = ele, last, second_last
            elif ele > second_last: 
                second_last, third_last = ele, second_last
            elif ele > third_last: 
                third_last = ele
        
        return min(last - third, third_last - first, second_last - second)
        
            
        