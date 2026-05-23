class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start=0
        end=0
        count=0
        res=0
        while end<len(nums):
            if nums[end]==1 and count<=1:
                end+=1
            elif nums[end]==0 and count==0:
                end+=1
                count+=1
            else:
                while nums[start]!=0:
                    start+=1
                start+=1
                count=0
            res=max(end-start,res)
        return res-1


            

        