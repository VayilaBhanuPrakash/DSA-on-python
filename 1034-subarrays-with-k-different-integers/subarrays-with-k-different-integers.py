class Solution:
    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:
        def atMost(nums,k):
            left = 0
            n = len(nums)
            count = 0
            h = {}
            for right in range(n):
                h[nums[right]] = h.get(nums[right], 0) + 1

                while len(h) > k:
                    h[nums[left]] -= 1
                    if h[nums[left]] == 0:
                        h.pop(nums[left])
                    left += 1
                
                count += right - left + 1
            return count
        return atMost(a,k) - atMost(a,k - 1)
