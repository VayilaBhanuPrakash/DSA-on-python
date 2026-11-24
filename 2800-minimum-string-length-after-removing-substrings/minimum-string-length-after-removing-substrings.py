class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ele in s:
            if ele == "B" and stack and stack[-1] == "A":
                stack.pop()
            elif ele == "D" and stack and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(ele)
        return len(stack)
        