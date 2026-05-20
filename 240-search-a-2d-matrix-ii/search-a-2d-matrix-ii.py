class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        col=len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False
                
            
        """rows,cols=0,0
        rows1,cols1=0,0
        l=len(matrix)
        l1=len(matrix[0])
        while cols<l1 and matrix[rows][cols]<=target:
            cols+=1
        while rows1<l and matrix[rows1][cols1]<=target:
            rows1+=1
        cols-=1
        rows1-=1
        for i in range(0,rows1+1):
            left=0
            right=cols
            while left<=right:
                mid=(left+right)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]<target:
                    left=mid+1
                else:
                    right=mid-1
        return False"""
        

        

        