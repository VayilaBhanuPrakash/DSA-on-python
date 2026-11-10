class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]

        res = []

        def dfs(par,count):
            nonlocal res
            if count < 0 or count > n:
                return
            if len(par) == 2 * n:
                if count == 0:
                    res.append(par)
                return
            dfs(par + '(', count + 1)
            dfs(par + ')', count - 1)
        dfs('',0)
        return res
        