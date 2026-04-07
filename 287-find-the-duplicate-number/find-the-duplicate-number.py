class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=set()
        for ele in nums:
            if ele not in l:
                l.add(ele)
            else:
                return ele
        