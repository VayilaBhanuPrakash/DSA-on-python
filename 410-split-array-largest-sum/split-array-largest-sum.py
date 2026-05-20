class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start=0
        end=0
        for ele in nums:
            start=max(start,ele)
            end+=ele
        while start<end:
            mid=start+(end-start)//2
            summ=0
            pieces=1
            for ele in nums:
                summ+=ele
                if summ>mid:
                    pieces+=1
                    summ=ele
            if pieces>k:
                start=mid+1
            else:
                end=mid
        return start

        