class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        Prefix=[0]*n
        Suffix=[0]*n
        Prefix[0]=nums[0]
        for i in range(1,n):
            Prefix[i]=min(nums[i],Prefix[i-1])
        Suffix[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            Suffix[i]=max(nums[i],Suffix[i+1])
        for i in range(1,n-1):
            if Prefix[i-1]<nums[i] and Suffix[i+1]>nums[i]:
                return True
        return False
        first=nums[0]
        second=float('inf')
        for i in range(1,len(nums)):
            if nums[i]<=first:
                first=nums[i]
            elif nums[i]<=second:
                second=nums[i]
            else:
                return True
        return False 
            
        