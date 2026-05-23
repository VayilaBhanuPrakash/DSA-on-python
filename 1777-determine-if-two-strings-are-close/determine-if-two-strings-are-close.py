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
            else:
                h2[ele]=1
        l1=[]
        l3=[]
        for keys in h1:
            l1.append(keys)
            l3.append(h1[keys])
        l2=[]
        l4=[]
        for keys in h2:
            l2.append(keys)
            l4.append(h2[keys])
        l1.sort()
        l2.sort()
        l3.sort()
        l4.sort()
        return l1==l2 and l3==l4
        