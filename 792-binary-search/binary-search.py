class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums,start,end,target):
            if end < start:
                return -1
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(nums, mid + 1, end, target)
            else:
                return binarySearch(nums, start, mid - 1, target)

        start = 0
        end = len(nums) - 1
        return binarySearch(nums, start, end, target)
        