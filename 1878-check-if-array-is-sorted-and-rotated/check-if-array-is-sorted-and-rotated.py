class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,i+n):
                if nums[(j-1)%n]>nums[j%n]:
                    break
            else:
                return True
        return False

        