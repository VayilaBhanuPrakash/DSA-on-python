class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        h = {0 : -1}

        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]

            remainder = prefix % k

            if remainder in h:
                if i - h[remainder] >= 2:
                    return True
                
            else:
                h[remainder] = i
        return False


        