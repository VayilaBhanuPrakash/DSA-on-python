class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        n = len(str1)
        for i in range(n,0,-1):
            if len(str1)%i==0 and len(str2)%i==0:
                string=str1[:i]
                if string*(len(str1)//i)==str1 and string*(len(str2)//i)==str2:
                    return string
        
        #return ""


        
        
        
        