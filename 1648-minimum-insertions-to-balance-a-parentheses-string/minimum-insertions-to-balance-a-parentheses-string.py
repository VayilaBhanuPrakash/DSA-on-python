class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        open = 0
        i = 0
        j = len(s)
        while i < j:
            if s[i] == "(":
                open += 1
            else:
                if i + 1 < j and s[i+1] == ")":
                    i += 1
                else:
                    res += 1
                if open == 0:
                    res += 1
                else:
                    open -= 1
            i += 1
        return  res + open * 2
                

        