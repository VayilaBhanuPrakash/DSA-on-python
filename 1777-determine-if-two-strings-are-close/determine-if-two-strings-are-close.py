class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1=len(word1)
        n2=len(word2)
        if n1!=n2:
            return False
        h1={}
        h2={}
        for ele in word1:
            if ele in h1:
                h1[ele]+=1
            else:
                h1[ele]=1
        for ele in word2:
            if ele in h2:
                h2[ele]+=1
            elif ele not in h1:
                return False
            else:
                h2[ele]=1
        l1=[]
        for values in h1.values():
            l1.append(values)
        l2=[]
        for values in h2.values():
            l2.append(values)
        l1.sort()
        l2.sort()
        return l1==l2


            
        