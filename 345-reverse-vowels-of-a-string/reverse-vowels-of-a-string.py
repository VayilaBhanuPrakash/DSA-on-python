class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        a=0
        b=len(s)-1
        while a<b:
            while a<b and l[a] not in vowels:
                a+=1
            while a<b and l[b] not in vowels:
                b-=1
            temp=l[a]
            l[a]=l[b]
            l[b]=temp
            a+=1
            b-=1
        return "".join(l)
        