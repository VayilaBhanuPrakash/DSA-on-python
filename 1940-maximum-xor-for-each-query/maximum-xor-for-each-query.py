class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        l=[0]*n
        first=0
        maxx=2**maximumBit-1
        for i in range(n):
            first=first^nums[i]
            l[n-i-1]=first^maxx
        return l

            

