class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []

        for ele in s:
            if ele == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ele)
        stack2 = []
        for ele in t:
            if ele == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ele)
        return stack1 == stack2
        