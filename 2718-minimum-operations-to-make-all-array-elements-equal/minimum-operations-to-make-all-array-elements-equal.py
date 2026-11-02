class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        ans = []
        for num in queries:
            i = 0
            j = n - 1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] <= num:
                    i = mid + 1
                else:
                    j = mid - 1
            left =  i * num - prefix_sum[i]
            right = prefix_sum[n] - prefix_sum[i] - (n - i) * num
            ans.append(left + right)
        return ans

        