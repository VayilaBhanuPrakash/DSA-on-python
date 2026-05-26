class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        h={}
        res=0
        for ele in word:
            if ele.islower():
                if ele in h and h[ele]==2:
                    h[ele]=3
                elif ele in h and h[ele]==3:
                    pass
                else:
                    h[ele]=1
            else:
                if ele.lower() in h and h[ele.lower()]<=2:
                    h[ele.lower()]=2
                else:
                    h[ele.lower()]=3
        for values in h.values():
            if values == 2:
                res+=1
        return res

        