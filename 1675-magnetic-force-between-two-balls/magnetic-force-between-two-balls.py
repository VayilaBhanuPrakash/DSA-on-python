class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        n = len(position)
        def isPossible(position,gap):
            balls = 1
            start = position[0]
            for i in range(1,n):
                if position[i] - start >= gap:
                    balls += 1
                    start = position[i]
            return balls >= m
        
        left = 1
        right = position[-1] - position[0]
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if isPossible(position,mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
            
        