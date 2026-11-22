class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = height[0]
        rightmax = height[n - 1]
        left = 0
        right = n - 1
        res = 0
        while left < right:
            if leftmax < rightmax:
                res += leftmax - height[left]
                left += 1
                leftmax = max(leftmax,height[left])
            else:
                res += rightmax - height[right]
                right -= 1
                rightmax = max(rightmax,height[right])
        return res

        


        