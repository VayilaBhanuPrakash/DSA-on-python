class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if ele in "({[":
                stack.append(ele)
            else:
                if ele == ")" and (not stack or stack.pop() != "("):
                    return False
                elif ele == "]" and (not stack or stack.pop() != "["):
                    return False
                elif ele == "}" and (not stack or stack.pop() != "{"):
                    return False
        return len(stack) == 0