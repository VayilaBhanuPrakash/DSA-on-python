class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[0 for i in range(n)]
        suf=[0 for i in range(n)]
        pro=1
        for i in range(n):
            pro=pro*nums[i]
            pre[i]=pro
        pro=1
        for j in range(n-1,-1,-1):
            pro=pro*nums[j]
            suf[j]=pro
        if n==2:
            nums[0],nums[1]=nums[1],nums[0]
            return nums
        nums[0]=suf[1]
        nums[n-1]=pre[n-1-1]
        for i in range(1,n-1):
            nums[i]=pre[i-1]*suf[i+1]
        return nums
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

        