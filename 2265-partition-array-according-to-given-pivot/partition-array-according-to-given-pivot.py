class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s = []
        l = []
        e = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                l.append(nums[i])
            elif nums[i] < pivot:
                s.append(nums[i])
            else:
                e.append(nums[i])

        return s + e + l
        