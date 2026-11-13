class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        majority = 1
        for i in range(1,len(nums)):
            if res == nums[i]:
                majority += 1
            else:
                if majority == 0:
                    res = nums[i]
                    majority = 1
                else:
                    majority -= 1
        return res

        