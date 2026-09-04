class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        max_prefix=[0]*n
        max_prefix[0]=nums[0]
        min_suffix=[0]*n
        min_suffix[n-1]=nums[n-1]
        for i in range(1,n):
            max_prefix[i]=max(max_prefix[i-1],nums[i])
            min_suffix[n-i-1]=min(min_suffix[n-i],nums[n-i-1])
        for i in range(n):
            if max_prefix[i]-min_suffix[i]<=k:
                return i
        return -1
        
            
            
            
        