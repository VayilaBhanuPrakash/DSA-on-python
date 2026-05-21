class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        h={}
        for ele in nums:
            if ele not in h:
                h[ele]=1
            elif h[ele]==1:
                h[ele]+=1
            else:
                return False
        return True
        