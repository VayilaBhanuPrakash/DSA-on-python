class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dup = [num for num in nums]
        for ele in dup:
            if ele == val:
                nums.remove(ele)
        return len(nums)
        