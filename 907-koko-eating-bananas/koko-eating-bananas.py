class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i = 0
        j = max(piles)
        n = len(piles)
        def eat(mid,h):
            hours = 0
            for ele in piles:
                if ele % mid == 0:
                    hours += ele // mid
                else:
                    hours += ele // mid + 1
            if hours > h:
                return False
            return True

        i = 1
        j = max(piles)
        while i <= j:
            mid = (i + j) // 2
            
            if eat(mid,h):
                j = mid - 1
            else:
                i = mid + 1
        return i