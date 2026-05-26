class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word=set(word)
        s=set()
        res=0
        for ele in word:
            if ele.lower() in s:
                res+=1
            else:
                s.add(ele.lower())
        return res
        