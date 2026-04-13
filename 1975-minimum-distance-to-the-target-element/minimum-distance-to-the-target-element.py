class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res=float('inf')
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]==target:
                res=min(res,abs(i-start))
            if nums[j]==target:
                res=min(res,abs(j-start))
            i+=1
            j-=1
        return res
        