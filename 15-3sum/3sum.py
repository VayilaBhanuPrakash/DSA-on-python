class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    l.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif summ < 0:
                    j += 1
                else:
                    k -= 1
        return l

        