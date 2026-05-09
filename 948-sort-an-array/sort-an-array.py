class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums,l,mid,r):
            c=[0 for i in range(r-l+1)]
            i=l
            j=mid+1
            k=0
            while i<=mid and j<=r:
                if  nums[i]<nums[j]:
                    c[k]=nums[i]
                    i+=1
                else:
                    c[k]=nums[j]
                    j+=1
                k+=1
            while i<=mid:
                c[k]=nums[i]
                i+=1
                k+=1
            while j<=r:
                c[k]=nums[j]
                j+=1
                k+=1
            k=0
            index=l
            while index<=r:
                nums[index]=c[k]
                index+=1
                k+=1
        def mergesort(nums,l,r):
            if l<r:
                mid=(l+r)//2
                mergesort(nums,l,mid)
                mergesort(nums,mid+1,r)
                merge(nums,l,mid,r)
        n=len(nums)
        mergesort(nums,0,n-1)
        return nums

        