class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        def fillBuckets(bloomDay,day):
            buckets = 0
            count = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    count += 1
                    if count == k:
                        buckets += 1
                        count = 0
                else:
                    count = 0
            return buckets >= m

        left = 1
        right = max(bloomDay)
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if fillBuckets(bloomDay,mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        