class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h={}
        for ele in arr:
            if ele in h:
                h[ele]+=1
            else:
                h[ele]=1
        res=-1
        for ele in arr:
            if h[ele]==ele:
                res=max(res,ele)
        return res
        