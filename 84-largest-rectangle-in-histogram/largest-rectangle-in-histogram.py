class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = []
        max_height = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] + 1 - 2

                height = h * width
                max_height = max(height, max_height)


            if not stack:
                width = i
            else:
                width = i - stack[-1] + 1 - 2
            height = width * heights[i]
            max_height = max(height, max_height)
            stack.append(i)

        return max_height
        