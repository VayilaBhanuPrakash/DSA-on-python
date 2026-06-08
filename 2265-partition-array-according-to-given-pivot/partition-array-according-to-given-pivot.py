class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        large = []
        p_count = 0
        for i in range(len(nums)):
            if nums[i] > pivot:
                large.append(nums[i])
            elif nums[i] < pivot:
                small.append(nums[i])
            else:
                p_count += 1
        for i in range(p_count):
            small.append(pivot)
        for ele in large:
            small.append(ele)
        return small
        