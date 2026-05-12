class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[j]+nums[k]==target:
                        return j,k 
        """h={}
        i=0
        for ele in nums:
            if target-ele in h:
                first=h[target-ele]
                second=i
                return first,second
            else:
                h[ele]=i
            i+=1"""
        