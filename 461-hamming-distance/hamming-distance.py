class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        ans = 0
        print(res)
        while res:
            res = res & (res - 1)
            ans += 1
        return ans



        