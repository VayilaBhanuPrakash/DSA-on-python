class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[[]]
        for num in nums:
            res1 = []
            for subset in res:
                res1.append(subset+[num])
            res.extend(res1)
        result = [list(i) for i in set(tuple(x) for x in res)]
        #res.sort()
        return result        