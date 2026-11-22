class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        res = [0] * (n - k + 1)
        queue = deque()
        for i in range(n):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res[i - k + 1] = nums[queue[0]]
        return res





        
        