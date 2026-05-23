class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=s[0]
        maxlen=1
        for i in range(len(s)):
            start=i
            end=len(s)-1
            while start<=end:
                if s[start]!=s[end]:
                    end-=1
                else:
                    st=start
                    en=end
                    while start<=end and (s[start]==s[end]):
                        start+=1
                        end-=1
                    if start>end:
                        if (en-st+1)>maxlen:
                            res=s[st:en+1]
                            maxlen=en-st+1
                    else:
                        end=en-1
                        start=st
        return res
        