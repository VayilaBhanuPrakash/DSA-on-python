class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ele in s:
            if ele == "(":
                stack.append(0)
            else:
                val = stack.pop()
                score = max(val * 2, 1)
                stack[-1] = stack[-1] + score
        return stack.pop()
        