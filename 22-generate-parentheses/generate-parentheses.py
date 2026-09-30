class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]

        res = []

        def dfs(par,count):
            nonlocal res
            if count < 0 or count > n:
                return
            if len(par) == n*2:
                if count == 0:
                    res.append(par)
                return
            if count < n:
                dfs(par+'(',count+1)
            if count > 0:
                dfs(par+')',count-1)
        dfs('(',1)
        return res
        