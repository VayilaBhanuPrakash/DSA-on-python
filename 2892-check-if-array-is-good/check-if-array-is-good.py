class Solution:
    def isGood(self, nums: List[int]) -> bool:
        h={}
        n=len(nums)
        if n==1:
            return False
        for ele in nums:
            if ele not in h:
                h[ele]=1
            else:
                h[ele]+=1
        for i in range(1,n-1):
            if i not in h:
                return False
            else:
                if h[i]==2:
                    return False
        if n-1 in h and h[n-1]==2:
            return True
        return False
        
        """nums.sort()
        n=len(nums)
        for i in range(1,n-1):
            if i!=nums[i-1]:
                return False
        if nums[-1]!=n-1 or nums[-2]!=n-1:
            return False
        return True"""
        
        