class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        close = 0
        for i in range(len(s)):
            if s[i] == "(":
                open += 1
            elif s[i] == ")":
                if open:
                    open -= 1
                else:
                    close += 1
        
        s = s.replace(")","",close)
        s = s.rsplit("(",open)
        
        return "".join(s)
        