class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        for i in range(len(s)):
            first=s[i]
            second=t[i]
            if first in dict_s:
                if dict_s[first]!=second:
                    return False
            else:
                dict_s[first]=second
            if second in dict_t:
                if dict_t[second]!=first:
                    return False
            else:
                dict_t[second]=first
        return True
            

            