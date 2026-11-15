class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[[]]
        for num in nums:
            res1=[]
            for subset in res:
                res1.append(subset+[num])
            for l in res1:
                if l not in res:
                    res.append(l)
        return res
        