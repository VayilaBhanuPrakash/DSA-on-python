class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        h = {}
        for ele in nums:
            if ele not in h:
                h[ele] = 1
            else:
                h[ele] += 1
        if k == len(nums):
            return max(nums)
        if k > 1:
            if h[nums[0]] == 1 and h[nums[-1]] == 1:
                if nums[0] > nums[-1]:
                    return nums[0]
                else:
                    return nums[-1]
            elif h[nums[0]] == 1 and h[nums[-1]] > 1:
                return nums[0]
            elif h[nums[0]] > 1 and h[nums[-1]] == 1:
                return nums[-1]
            else:
                return -1
        else:
            maxx = -1
            for key in h:
                if h[key] == 1:
                    maxx = max(maxx,key)
            return maxx