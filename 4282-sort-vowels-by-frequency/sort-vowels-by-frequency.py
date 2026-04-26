class Solution:
    def sortVowels(self, s: str) -> str:
        vowels={"a","e","i","o","u"}
        dictt={}
        n=len(s)
        first_index={}
        for i in range(n):
            if s[i] in vowels:
                dictt[s[i]]=dictt.get(s[i],0)+1
                if s[i] not in first_index:
                    first_index[s[i]]=i
        sorted_dictt=dict(sorted(dictt.items(),key=lambda x:(-x[1], first_index[x[0]])))
        l=""
        for key in sorted_dictt:
            l=l+key*sorted_dictt[key]
        res=""
        j=0
        for i in range(n):
            if s[i] in vowels:
                res+=l[j]
                j+=1
            else:
                res+=s[i]
        return res
        