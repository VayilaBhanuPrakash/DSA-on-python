class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h={}
        for ele in nums:
            if ele in h.keys():
                return True
            else:
                h[ele]=0
        return False
        