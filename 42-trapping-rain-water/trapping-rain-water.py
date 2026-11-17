class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n -1
        leftmax = height[i]
        rightmax = height[j]
        res = 0
        while i < j:
            if leftmax < rightmax:
                res += leftmax - height[i]
                i += 1
                leftmax = max(leftmax, height[i])
            else:
                res += rightmax - height[j]
                j -= 1
                rightmax = max(rightmax, height[j])
        return res


        

        


        