class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[]
        for i in range(rowIndex+1):
            row=[]
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(l[i-1][j-1]+l[i-1][j])
            l.append(row)
        return l[rowIndex]
        