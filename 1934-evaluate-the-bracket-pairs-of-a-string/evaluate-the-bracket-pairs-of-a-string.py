class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res = ""
        stack = []
        h = {}
        for key,val in knowledge:
            h[key] = val
        for ele in s:
            if ele == ")":
                key = "".join(stack[1:])

                res = res + h.get(key,"?")
    
                stack = []
            elif ele.islower() and not stack:
                res = res + ele
            else:
                stack.append(ele)
        return res



        