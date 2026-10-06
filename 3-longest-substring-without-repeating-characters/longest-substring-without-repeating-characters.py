class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        st = set()
        for j in range(len(s)):
            while s[j] in st:
                st.remove(s[i])
                i += 1
            st.add(s[j])
            res = max(res,j-i+1)
        return res
        

            

            
        