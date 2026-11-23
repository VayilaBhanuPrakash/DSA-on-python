class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [-1] * n
        stack = [nums[-1]]
        for i in range(2 * n - 2, -1, -1):
            index = i % n
            while stack and stack[-1] <= nums[index]:
                stack.pop()
            
            if i < n and stack:
                res[i] = stack[-1]
            stack.append(nums[index])
        return res
        


        