class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        b = nums[-1]
        for i in range(a,-1,-1):
            if a % i == 0 and b % i == 0:
                return i

        