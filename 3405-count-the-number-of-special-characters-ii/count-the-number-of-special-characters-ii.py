class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        h={}
        res=0
        for ele in word:
            ch=ele.lower()
            if ele.islower():
                if ele in h and h[ele]==2:
                    h[ele]=3
                elif ele in h and h[ele]==3:
                    pass
                else:
                    h[ele]=1
            else:
                if ch in h and h[ch]==1:
                    h[ch]=2
                elif ch in h and h[ch]==2:
                    pass
                else:
                    h[ch]=3
        for values in h.values():
            if values == 2:
                res+=1
        return res

        