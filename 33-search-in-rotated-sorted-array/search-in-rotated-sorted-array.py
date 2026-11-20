class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1 and nums[0] == target:
            return 0
        
        i = 0
        j = n - 1
        pivot = -1

        while i <= j:
            mid = i + (j - i) // 2
            if mid + 1 < n and nums[mid] > nums[mid + 1]:
                pivot = mid
                break
            elif nums[i] <=nums[mid]:
                i = mid + 1
            else:
                j = mid -1
        if target > nums[-1]:
            i = 0
            j = pivot
        else:
            i = pivot + 1
            j = n - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

        