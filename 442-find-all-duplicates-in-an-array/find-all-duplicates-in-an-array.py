class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        sett=set()
        for ele in nums:
            if ele in sett:
                res.append(ele)
            else:
                sett.add(ele)
        return res
        