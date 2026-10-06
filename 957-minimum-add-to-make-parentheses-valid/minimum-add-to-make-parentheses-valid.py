class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = []
        for ele in s:
            if ele == "(":
                stack.append(ele)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)
        