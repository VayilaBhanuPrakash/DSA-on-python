class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s_t={}
        dict_t_s={}
        for i in range(len(s)):
            first=s[i]
            second=t[i]
            if first not in dict_s_t:
                dict_s_t[first]=second
            else:
                if dict_s_t[first]!=second:
                    return False
            if  second not in dict_t_s:
                dict_t_s[second]=first
            else:
                if dict_t_s[second]!=first:
                    return False
        return True
      

            