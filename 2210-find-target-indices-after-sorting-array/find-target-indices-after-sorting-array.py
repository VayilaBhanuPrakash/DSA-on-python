class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        equal = 0
        small = 0
        for ele in nums:
            if ele < target:
                small += 1
            elif ele == target:
                equal += 1
        return [i for i in range(small,small+equal)]
        