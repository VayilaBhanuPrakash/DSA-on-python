class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1={}
        h2={}
        for ele in s:
            if ele not in h1:
                h1[ele]=1
            else:
                h1[ele]+=1
        for ele in t:
            if ele not in h2:
                h2[ele]=1
            else:
                h2[ele]+=1
        if len(h1)!=len(h2):
            return False
        for char in h1.keys():
            if char in h2.keys() and h1[char]==h2[char]:
                pass
            else:
                return False
        return True
        
        