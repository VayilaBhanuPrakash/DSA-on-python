class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        i=0
        j=0
        maxx=0
        h={}
        while j<k:
            sum+=nums[j]
            if nums[j] in h:
                h[nums[j]]+=1
            else:
                h[nums[j]]=1
            j+=1
        if len(h)==k:
            maxx=sum
        while i<len(nums)-k:
            sum-=nums[i]
            sum+=nums[j]
            h[nums[i]]-=1
            if h[nums[i]]==0:
                h.pop(nums[i])
            if nums[j] in h:
                h[nums[j]]+=1
            else:
                h[nums[j]]=1
            if len(h)==k:
                maxx=max(maxx,sum)
            i+=1
            j+=1
        return maxx


        
        
        