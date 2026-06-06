class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        res = [1 for i in range(n)]
        for i in range(k):
            for j in range(n):
                if j == 0:
                    continue
                else:
                    res[j] = res[j] + res[j-1]
        return res[n-1] % (10**9 + 7)

        