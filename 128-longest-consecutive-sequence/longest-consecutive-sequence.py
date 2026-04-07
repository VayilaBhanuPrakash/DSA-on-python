class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0 or n==1:
            return n
        nums.sort()
        first=nums[0]
        count=1
        Max_count=1
        for i in range(1,n):
            if first==nums[i]-1:
                count+=1
            elif first==nums[i]:
                pass
            else:
                Max_count=max(Max_count,count)
                count=1
            #print(count,first,nums[i])
            first=nums[i]
        Max_count=max(Max_count,count)
        return Max_count


        