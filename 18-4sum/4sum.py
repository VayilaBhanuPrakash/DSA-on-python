class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                k=j+1
                l=n-1
                while k<l:
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total==target:
                        if [nums[i],nums[j],nums[k],nums[l]] not in res:
                            res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                    elif total>target:
                        l-=1
                    else:
                        k+=1
        return res
                    
        