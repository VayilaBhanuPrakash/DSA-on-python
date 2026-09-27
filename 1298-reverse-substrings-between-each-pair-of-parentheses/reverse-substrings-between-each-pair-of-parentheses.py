class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for ch in s:
            if ch ==  "(":
                stack.append("")
            elif ch.islower():
                stack[-1] += ch
                
            else:
                temp = stack.pop()
                stack[-1] += temp[::-1]
        return stack[-1]

        