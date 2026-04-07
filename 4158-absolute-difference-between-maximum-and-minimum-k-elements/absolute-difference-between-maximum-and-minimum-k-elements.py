class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        First_sum=0
        Second_sum=0
        while k!=0:
            First_sum+=nums[i]
            Second_sum+=nums[j]
            i+=1
            j-=1
            k-=1
        return Second_sum-First_sum


        