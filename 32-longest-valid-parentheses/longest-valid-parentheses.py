class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = []
        close = []

        for i in range(len(s)):
            if s[i] == "(":
                open.append(i)
            else:
                if open:
                    open.pop()
                else:
                    close.append(i)
        open.append(-1)
        open.append(len(s))
        open.extend(close)
        open.sort()
        res = 0
        for i in range(len(open) - 1):
            res = max(res, open[i + 1] - open[i] - 1)
        
        return res
        