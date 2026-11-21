class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        def lessElements(matrix,val):
            row = rows - 1
            col = 0
            count = 0
            while row >= 0 and col < cols:
                if matrix[row][col] > val:
                    row -= 1
                else:
                    count += row + 1
                    col += 1
            return count



        rows = len(matrix)
        cols = len(matrix[0])
        left = matrix[0][0]
        right = matrix[rows - 1][cols - 1]
        while left <= right:
            mid = left + (right - left) // 2
            if lessElements(matrix,mid) < k:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res
        