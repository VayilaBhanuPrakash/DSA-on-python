class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        """nums.sort()
        i=0
        j=len(nums)-1
        First_sum=0
        Second_sum=0
        while k!=0:
            First_sum+=nums[i]
            Second_sum+=nums[j]
            i+=1
            j-=1
            k-=1
        return Second_sum-First_sum"""
        nums.sort()
        j=len(nums)-1
        First_sum=0
        Second_sum=0
        while k!=0:
            First_sum+=nums[k-1]
            Second_sum+=nums[j]
            j-=1
            k-=1
        return Second_sum-First_sum


        