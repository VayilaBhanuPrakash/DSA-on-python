class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i<n:
            if nums[i]<1  or nums[i]>n:
                i+=1
            else:
                correct=nums[i]-1
                if nums[i]!=nums[correct]:
                    nums[i],nums[correct]=nums[correct],nums[i]
                else:
                    i+=1 
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1     