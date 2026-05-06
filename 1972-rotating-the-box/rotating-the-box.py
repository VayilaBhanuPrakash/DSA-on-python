class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows=len(boxGrid)
        cols=len(boxGrid[0])
        res=[[0 for i in range(rows)] for j in range(cols)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if j<cols-1 and boxGrid[i][j]=="#" and res[j+1][i]==".":
                    res[j][i]=boxGrid[i][j]
                    res[j][i],res[j+1][i]=res[j+1][i],res[j][i]
                    j=j+1
                    while j<cols-1 and res[j][i]=="#" and res[j+1][i]==".":
                        res[j][i],res[j+1][i]=res[j+1][i],res[j][i]
                        j+=1

                else:
                    res[j][i]=boxGrid[i][j]
        """l=[]
        for ele in res:
            l.append(ele[::-1])"""
        return [rows[::-1] for rows in res]
        