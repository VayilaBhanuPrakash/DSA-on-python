class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        l=[]
        res=""
        for i in range(n):
            if s[i].isalnum():
                res+=s[i]
            else:
                if len(res)>0:
                    l.append(res)
                    res=""
        if res:
            l.append(res)
        result=""
        for j in range(len(l)-1,-1,-1):
            result+=" "
            result+=l[j]
        return result[1:]

        
        