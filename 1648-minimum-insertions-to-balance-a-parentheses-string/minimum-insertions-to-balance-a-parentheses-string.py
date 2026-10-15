class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))","}")
        res = 0
        stack = []
        for ele in s:
            if ele == "(":
                stack.append(ele)
            elif ele == "}" and stack and stack[-1] == "(":
                stack.pop()
            elif ele == "}" and not stack:
                res += 1
            elif ele == ")" and stack and stack[-1] == "(":
                res += 1
                stack.pop()
            elif ele == ")" and not stack:
                res += 2
        return res + len(stack)*2
                

        
        