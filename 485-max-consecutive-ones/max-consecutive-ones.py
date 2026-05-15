class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        count=0
        for ele in nums:
            if ele==1:
                count+=1
            else:
                maxx=max(maxx,count)
                count=0
        maxx=max(maxx,count)
        return maxx
        