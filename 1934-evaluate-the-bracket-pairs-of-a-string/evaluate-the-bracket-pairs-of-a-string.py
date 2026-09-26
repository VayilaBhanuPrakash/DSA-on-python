class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res = ""
        stack = []
        h = {}
        for i in range(len(knowledge)):
            h[knowledge[i][0]] = knowledge[i][1]
        for ele in s:
            if ele == ")":
                key = "".join(stack[1:])
                if key in h:
                    res = res + h[key]
                else:
                    res = res + "?"
                stack = []
            elif ele.islower() and not stack:
                res = res + ele
            else:
                stack.append(ele)
        return res
        