class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def findDays(weights, mid):
            dayss = 0
            load = 0
            for ele in weights:
                load += ele
                if load > mid:
                    dayss += 1
                    load = ele
            dayss += 1
            return dayss
        left = max(weights)
        right = sum(weights)
        res = right
        while left <= right:
            mid = left + (right - left) // 2
            if findDays(weights,mid) > days:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res

        