class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = ""
        for ele in s:
            if ele == "(":
                count += 1
                if count > 1:
                    res = res + ele
            else:
                count -= 1
                if count:
                    res = res + ele
        return res
        