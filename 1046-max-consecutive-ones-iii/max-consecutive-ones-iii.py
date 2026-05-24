class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums)<=k:
            return len(nums)
        start=0
        end=0
        count=0
        res=0
        flag=0
        while end<len(nums):
            if nums[end]==1 and count<=k:
                end+=1
                flag=1
            elif nums[end]==0 and count<k:
                end+=1
                count+=1
            else:
                res=max(end-start,res)
                while nums[start]!=0:
                    start+=1
                start+=1
                count-=1
        res=max(end-start,res)
        if flag==0 and count==k:
            return k
        if res==0 and count<=k:
            return len(nums)
        return res
        