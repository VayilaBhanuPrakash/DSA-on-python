class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        l=[]
        count=1
        i=0
        j=0
        while j<n:
            if nums[i]+1<nums[j]:
                i+=1
                j+=1
            while j<n and (nums[i]==nums[j] or nums[i]+1==nums[j]):
                j+=1
            if nums[i]!=nums[j-1]:
                l.append(j-i)
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
        if not l:
            return 0
        return max(l)

        


            

        