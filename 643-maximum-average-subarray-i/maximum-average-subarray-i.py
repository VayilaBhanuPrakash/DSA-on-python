class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maxx=summ
        for i in range(k,len(nums)):
            summ=summ-nums[i-k]+nums[i]
            maxx=max(maxx,summ)
        return maxx/k

        """i=0
        j=k
        summ=0
        for index in range(k):
            summ+=nums[index]
        maxx=summ
        while j<len(nums):
            summ-=nums[i]
            summ+=nums[j]
            j+=1
            i+=1
            maxx=max(maxx,summ)
        return maxx/k"""


        