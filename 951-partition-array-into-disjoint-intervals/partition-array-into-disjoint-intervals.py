class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n=len(nums)
        right_min=[0]*n
        right_min[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            right_min[i]=min(nums[i],right_min[i+1])
        left_max=float('-inf')
        print(right_min)
        for i in range(n-1):
            left_max=max(left_max,nums[i])
            if left_max<=right_min[i+1]:
                return i+1
        return n-1

        