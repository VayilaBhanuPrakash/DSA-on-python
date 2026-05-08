class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        for i in range(k):
            sum+=nums[i]
        maxx=sum
        for j in range(k,len(nums)):
            sum-=nums[j-k]
            sum+=nums[j]
            maxx=max(maxx,sum)
        return maxx/k
        