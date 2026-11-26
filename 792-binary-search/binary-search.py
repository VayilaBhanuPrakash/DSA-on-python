class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find(nums,start,end,target):
            if end < start:
                return -1
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return find(nums, mid + 1, end, target)
            else:
                return find(nums, start, mid - 1, target)


        return find(nums, 0, len(nums) - 1, target)

        