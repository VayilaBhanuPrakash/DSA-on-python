class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """dict_s={}
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
        return True"""
        h={}
        for i in range(len(s)):
            #first=s[i]
            #second=t[i]
            if s[i] in h.keys() and h[s[i]]!=t[i]:
                return False
            elif s[i] not in h.keys() and t[i] in h.values():
                return False
            else:
                h[s[i]]=t[i]
        return True

            