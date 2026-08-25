class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[False for i in range(n)] for j in range(n)]
        left = 0
        right = n - 1
        first = 0
        last = n - 1

        i = 1
        while left <= right and first <= last:

            for j in range(left,right + 1):
                res[first][j] = i
                i += 1
            first += 1
            for j in range(first,last + 1):
                res[j][right] = i
                i += 1
            right -= 1
            if first < last:
                for j in range(right,left - 1,-1):
                    res[last][j] = i
                    i += 1
                last -= 1
            if left <= right:
                for j in range(last,first - 1,-1):
                    res[j][left] = i
                    i += 1
                left += 1
        return res
                
        
        