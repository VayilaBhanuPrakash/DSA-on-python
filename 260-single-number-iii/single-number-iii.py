class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        h={}
        for ele in nums:
            if ele in h:
                h[ele]+=1
            else:
                h[ele]=1
        res=[]
        for i in h.keys():
            if h[i]==1:
                res.append(i)
        return res