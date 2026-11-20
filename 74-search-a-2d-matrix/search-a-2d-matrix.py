class Solution:    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows
        valid_row = -1
        def valid_row(matrix,target):
            rows = len(matrix)
            cols = len(matrix[0])
            left = 0
            right = rows - 1
            while left <= right:
                mid = left + (right - left) // 2

                if matrix[mid][0] > target:
                    right = mid - 1
                elif matrix[mid][0] <= target and matrix[mid][cols - 1] >= target:
                    return mid
                elif matrix[mid][0] < target:
                    left = mid + 1
            return -1
        
        def row_search(arr,target):
            left = 0
            right = len(arr)
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        if valid_row(matrix,target) == -1:
            return False
        
        row = valid_row(matrix,target)

        return row_search(matrix[row],target)
        

        

        


        






        