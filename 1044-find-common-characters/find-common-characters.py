class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=[]
        for ele in words:
           h = {}
           for letters in ele:
                if letters in h:
                    h[letters] += 1
                else:
                    h[letters] = 1
           l.append(h)
        res = []
        for keys in l[0]:
            minn = l[0][keys]
            for i in range(1,len(l)):
                if keys not in l[i]:
                    minn = 0
                    break
                else:
                    minn = min(minn,l[i][keys])
            res.extend([keys]*minn)
        return res
                    
                
                

        

