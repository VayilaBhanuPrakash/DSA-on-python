class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0

            for ele in nums:
                if (ele >> i) & 1:
                    count += 1
            
            if count % 3:
                res = res | (1 << i)

        if res >= (1 << 31):
            res -= (1 << 32)
        return res 

        