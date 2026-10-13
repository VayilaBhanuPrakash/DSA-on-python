class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        res = 0
        l = []
        for i in nums:
            if i < 0:
                l.append(-i)
            else:
                l.append(i)
        l.sort()
        n = len(nums)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n // 2
        for i in range(n):
            res -= l[i] ** 2
        for i in range(n,len(nums)):
            res += l[i] ** 2
        return res
        