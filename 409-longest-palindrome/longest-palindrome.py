class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictt={}
        for i in range(len(s)):
            if s[i] not in dictt:
                dictt[s[i]]=1
            else:
                dictt[s[i]]+=1
        count=0
        odd_count=False
        for value in dictt.values():
            if value%2==0:
                count+=value
            else:
                count+=value-1
                odd_count=True
        if odd_count:
            return count+1
        return count


        