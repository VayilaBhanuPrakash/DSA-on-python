class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        h = {}
        left = 0
        res = 0
        n = len(fruits)
        for right in range(n):
            h[fruits[right]] = h.get(fruits[right], 0) + 1

            while len(h) > 2:
                h[fruits[left]] -= 1
                if h[fruits[left]] == 0:
                    h.pop(fruits[left])
                left += 1
            res = max(res, right - left + 1)
        return res
        