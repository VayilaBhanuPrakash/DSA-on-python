class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h1={}
        for ele in nums1:
            if ele in h1:
                h1[ele]+=1
            else:
                h1[ele]=1
        h2={}
        for ele in nums2:
            if ele in h2:
                h2[ele]+=1
            else:
                h2[ele]=1
        res=[]
        for keys in h1.keys():
            if keys in h2:
                minn=min(h1[keys],h2[keys])
                for i in range(minn):
                    res.append(keys)
        return res
            
        
        