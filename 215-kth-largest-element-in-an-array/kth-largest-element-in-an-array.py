import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        heap=[-nums[i] for i in range(n)]
        #print(heap)
        heapq.heapify(heap)
        for i in range(k):
            res=heapq.heappop(heap)
        return -res

        