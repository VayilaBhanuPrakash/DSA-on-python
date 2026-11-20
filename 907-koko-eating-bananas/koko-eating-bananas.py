class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def CanEat(piles, mid):
            time = 0
            for ele in piles:
                if ele % mid == 0:
                    time += ele // mid
                else:
                    time += ele // mid + 1
            if time <= h:
                return True
            return False

        start = 1
        end = max(piles)
        while start <= end:
            mid = start + (end - start) // 2
            if CanEat(piles, mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
