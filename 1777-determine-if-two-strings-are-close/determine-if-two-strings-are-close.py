class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
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
        l=[]
        for values in h1.values():
            l.append(values)
        for values in h2.values():
            if values in l:
                l.remove(values)
        return len(l)==0
        