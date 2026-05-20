class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        h={}
        common=0
        res=[]
        for i in range(len(A)):
            if A[i] in h:
                h[A[i]]+=1
            else:
                h[A[i]]=1
            if B[i] in h:
                h[B[i]]+=1
            else:
                h[B[i]]=1
            res.append((i+1)*2-len(h))
            
        return res
            
            
        