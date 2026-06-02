class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h={}
        for ele in nums:
            if ele in h:
                h[ele]+=1
            else:
                h[ele]=1
        for ele in h:
            if h[ele]>=2:
                return ele
            
        
        