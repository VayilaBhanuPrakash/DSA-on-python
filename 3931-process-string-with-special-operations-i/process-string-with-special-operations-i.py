class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for letters in s:
            if letters == "#":
                res = res + res
            elif letters == "%":
                res = res[::-1]
            elif letters == "*":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(letters)
        return "".join(res)
        