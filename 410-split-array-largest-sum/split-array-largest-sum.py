class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start=0
        end=0
        for ele in nums:
            start=max(start,ele)
            end=end+ele
        #binary search
        while start<end:
            #try for the middle as potential answer
            mid=start+(end-start)//2
            #calculate how many pieces we can divide with is max sum
            sum=0
            pieces=1
            for ele in nums:
                if sum+ele>mid:
                    #we cannot add this to the subarray-->make new subarry
                    #so new subarray consists one ele that is ele then sum=ele
                    pieces+=1
                    sum=ele
                else:
                    sum+=ele
            if pieces>k:
                start=mid+1
            else:
                end=mid
        return start
            


        

        