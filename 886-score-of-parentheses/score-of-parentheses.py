class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            else:
                count -= 1
                if s[i - 1] == "(":
                    res = res + (1 << count)

        return res
        