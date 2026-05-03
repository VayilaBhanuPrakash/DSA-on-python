class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett=set()
        for ele in nums:
            if ele in sett:
                return True
            sett.add(ele)
        return False
        