class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        flag=0
        flag1=0
        prod=1
        for ele in nums:
            if ele==0:
                flag+=1
            else:
                flag1=1
                prod=prod*ele
        l=[]
        if flag==0:
            for i in range(len(nums)):
                l.append(prod//nums[i])
        else:
            for i in range(len(nums)):
                if nums[i]==0 and flag1==1 and flag==1:
                    l.append(prod)
                else:
                    l.append(0)
        return l

        