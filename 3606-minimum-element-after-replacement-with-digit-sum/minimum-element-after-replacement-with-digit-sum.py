class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=float('inf')
        for ele in nums:
            summ=0
            val=ele
            while val:
                rem=val%10
                val=val//10
                summ+=rem
            res=min(res,summ)
        return res




        