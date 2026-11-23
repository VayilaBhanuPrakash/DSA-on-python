class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {nums2[-1] : -1}
        stack = [nums2[-1]]
        n = len(nums2)
        for i in range(n - 2, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                h[nums2[i]] = stack[-1]
            else:
                h[nums2[i]] = -1
            stack.append(nums2[i])
        
        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = h[nums1[i]]
        return res
        


        