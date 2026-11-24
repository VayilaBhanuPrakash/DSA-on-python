class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        def maxArea(arr):
            maximum = 0
            stack = []
            for i in range(len(arr) + 1):
                h = 0 if i == len(arr) else arr[i]
                while stack and arr[stack[-1]] > h:
                    height = arr[stack.pop()]
                    width = i if not stack else i - stack[-1] + 1 - 2
                    area = height * width
                    maximum = max(maximum, area)

                stack.append(i)
            return maximum
        
        max_area = 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1

            max_area = max(max_area, maxArea(heights))
        
        return max_area
        