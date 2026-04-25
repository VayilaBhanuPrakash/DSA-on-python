class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maxx=summ
        for i in range(k,len(nums)):
            summ-=nums[i-k]
            summ+=nums[i]
            maxx=max(maxx,summ)
        return maxx/k
        