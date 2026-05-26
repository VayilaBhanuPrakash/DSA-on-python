class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word=set(word)
        h={}
        for ele in word:
            if ele.islower():
                if ele.upper() in h:
                    h[ele]=2
                else:
                    h[ele]=1
            else:
                if ele.lower() in h:
                    h[ele]=2
                else:
                    h[ele]=1
        res=0
        for values in h.values():
            if values==2:
                res+=1
        return res
        