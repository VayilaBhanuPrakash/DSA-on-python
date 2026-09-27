class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for i in range(len(s)):
            if s[i] == ")":
                last = []
                while stack:
                    if stack and stack[-1] != "(":
                        last.append(stack.pop())
                    elif stack and stack[-1] == "(":
                        stack.pop()
                        stack.extend(last)
                        break
                if stack and stack[0] != "(":
                    res = res + "".join(stack)
                    stack = []

            elif s[i].islower() and not stack:
                res = res +s[i]
            elif s[i] == "(":
                stack.append(s[i])
            else:
                stack.append(s[i])
        return res
        