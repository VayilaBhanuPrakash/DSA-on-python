class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        def canReach(dist, mid):
            time = 0
            for i in range(n - 1):
                time += (dist[i] // mid) if (dist[i] % mid) == 0 else (dist[i] // mid) + 1
            time += dist[n - 1] / mid
            return time <= hour
        n = len(dist)
        left = 1
        right = 10 ** 7
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if canReach(dist, mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res



        