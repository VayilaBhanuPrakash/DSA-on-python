class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maxx=summ
        for i in range(k,len(nums)):
            summ=summ-nums[i-k]+nums[i]
            maxx=max(maxx,summ)
        return maxx/k
        