class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        h={}
        nums1=set(nums1)
        nums2=set(nums2)
        for ele in nums1:
            h[ele]=1
        for ele in nums2:
            if ele in h:
                h[ele]=3
            else:
                h[ele]=2
        res=[[],[]]
        for keys in h.keys():
            if h[keys]==1:
                res[0].append(keys)
            elif h[keys]==2:
                res[1].append(keys)
        return res
        