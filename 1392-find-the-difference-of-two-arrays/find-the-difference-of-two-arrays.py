class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[[],[]]
        nums1=set(nums1)
        nums2=set(nums2)
        for ele in nums1:
            if ele not in nums2:
                res[0].append(ele)
        for ele in nums2:
            if ele not in nums1:
                res[1].append(ele)
        return res
