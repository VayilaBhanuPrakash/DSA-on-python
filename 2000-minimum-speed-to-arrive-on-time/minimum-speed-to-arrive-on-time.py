class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        def timeTaken(dist, mid):
            time = 0
            for i in range(n):
                if i == n - 1:
                    time += dist[i] / mid
                else:
                    time += (dist[i] // mid) if (dist[i] % mid) == 0 else (dist[i] // mid) + 1
            return time
        n = len(dist)
        left = 1
        right = 10 ** 7
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if timeTaken(dist, mid) <= hour:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        