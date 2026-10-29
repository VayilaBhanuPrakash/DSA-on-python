class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        i = 0
        j = piles[-1]
        n = len(piles)

        while i <= j:
            mid = (i + j) // 2
            if mid == 0:
                i = 1
                continue
            hours = 0
            for ele in piles:
                if ele % mid == 0:
                    hours += ele // mid
                else:
                    hours += ele // mid + 1
            #print(mid,hours)
            
            if hours > h:
                i = mid + 1
            else:
                j = mid - 1
        return i