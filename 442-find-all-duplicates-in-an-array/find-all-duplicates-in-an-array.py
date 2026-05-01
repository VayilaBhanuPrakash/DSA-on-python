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
        """res=[]
        h={}
        for ele in nums:
            if ele in h:
                res.append(ele)
            else:
                h[ele]=1
        return res"""

        