class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i = 0
        j = max(piles)
        piles.sort()
        if len(piles) == 1:
            if piles[0] % h == 0:
                return piles[i] // h
            else:
                return piles[0] // h + 1
            return piles[0] // h + 1
        while i <= j:
            mid = i + (j-i) // 2
            if mid == 0:
                i = 1
                continue
            hours = 0
            for c in range(len(piles)):
                if piles[c] % mid == 0:
                    hours += piles[c] // mid
                else:
                    hours += piles[c] // mid + 1

            if hours > h:
                i = mid + 1
            else:
                j = mid - 1
        return i
