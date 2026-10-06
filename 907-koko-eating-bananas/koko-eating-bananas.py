class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i = 0
        j = max(piles)
        piles.sort()
        n = len(piles)
        while i <= j:
            mid = i + (j-i) // 2
            if mid == 0:
                i = 1
                continue
            hours = 0
            for c in range(n):
                if piles[c] % mid == 0:
                    hours += piles[c] // mid
                else:
                    hours += piles[c] // mid + 1

            if hours > h:
                i = mid + 1
            else:
                j = mid - 1
        return i
        