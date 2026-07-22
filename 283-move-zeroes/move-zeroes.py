class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for j in range(pos,len(nums)):
            nums[j]=0
        """
        Do not return anything, modify nums in-place instead.
        """
        