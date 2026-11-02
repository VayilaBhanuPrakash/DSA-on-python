class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        ans = []
        n = len(nums)
        for num in queries:
            i = 0
            j = n
            while i < j:
                mid = (i + j) // 2
                if nums[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            left_cost = num * i - prefix_sum[i]
            right_cost = (prefix_sum[n] - prefix_sum[i]) - num * (n - i)
            ans.append(left_cost + right_cost)
        return ans
            
        
            
        