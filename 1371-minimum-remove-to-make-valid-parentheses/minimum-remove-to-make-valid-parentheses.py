class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = []
        close = []
        for i in range(len(s)):
            if s[i] == "(":
                open.append(i)
            elif s[i] == ")":
                if open:
                    open.pop()
                else:
                    close.append(i)
        
        stack = []
        for i in range(len(s)):
            if i not in open and i not in close:
                stack.append(s[i])
        
        return "".join(stack)
        