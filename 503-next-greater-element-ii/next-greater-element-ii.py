class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        n=len(nums)
        l=[]
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack:
                l.append(stack[-1])
            else:
                l.append(-1)
            stack.append(nums[i])
        return l[::-1][:n//2]

            

        