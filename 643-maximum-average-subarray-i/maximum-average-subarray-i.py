class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
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
        return maxx/k


        