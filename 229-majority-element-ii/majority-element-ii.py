class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        for ele in nums:
            if ele not in h:
                h[ele] = 1
            else:
                h[ele] += 1
        res =[]
        for keys in h:
            if h[keys] > (len(nums)//3):
                res.append(keys)
        return res        