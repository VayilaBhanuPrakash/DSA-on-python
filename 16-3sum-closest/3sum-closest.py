class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest=float('inf')
        for i in range(n-2):
            left=i+1
            right=n-1 
            while left<right:
                target1=nums[i]+nums[left]+nums[right]
                if abs(target-target1)<abs(target-closest):
                    closest=target1     
                if target1<target:
                    left+=1
                elif target1>target:
                    right-=1
                else:
                    return target1 #exact match
        return closest
        