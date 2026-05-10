class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        stack=[]
        h={}
        for i in range(n-1,-1,-1):
            while stack and nums2[i]>=stack[-1]:
                stack.pop()
            if stack:
                h[nums2[i]]=stack[-1]
            else:
                h[nums2[i]]=-1
            stack.append(nums2[i])
        res=[]
        for ele in nums1:
            res.append(h[ele])
        return res


        