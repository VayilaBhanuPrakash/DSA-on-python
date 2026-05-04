class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h={}
        res=[]
        for ele in nums1:
            h[ele]=1
        for ele in nums2:
            if ele in h:
                h[ele]=2
        for ele in h.keys():
            if h[ele]==2:
                res.append(ele)
        return res

        