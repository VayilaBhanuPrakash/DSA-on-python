class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for ele in nums:
            if ele not in h:
                h[ele] = 1
            else:
                h[ele] += 1
        for keys in h:
            if h[keys] > len(nums)/2:
                return keys

        