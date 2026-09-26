class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res = ""
        h = {}
        for i in range(len(knowledge)):
            h[knowledge[i][0]] = knowledge[i][1]

        start = -1
        end = -1
        for i in range(len(s)):
            if s[i] == ")":
                key = "".join(s[start:end])

                res = res + h.get(key,"?")
                start = -1
                end = -1
    
            elif s[i].islower() and start == -1 and end == -1:
                res = res + s[i]
            elif s[i] == "(":
                start = i + 1
                end = i + 1
            else:
                end = end + 1
        return res
        