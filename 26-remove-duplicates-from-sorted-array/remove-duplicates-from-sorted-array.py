class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = [num for num in nums]
        for i in range(1,len(nums)):
            if dup[i-1] == dup[i]:
                nums.remove(dup[i-1])
        return len(nums)

        