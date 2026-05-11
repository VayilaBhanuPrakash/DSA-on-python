class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]
            while num>0:
                res.append(num%10)
                num=num//10
        i=0
        j=len(res)-1
        print(res)
        while i<j:
            temp=res[i]
            res[i]=res[j]
            res[j]=temp
            i+=1
            j-=1
        return res
        