# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        i=0
        j=mountainArr.length()-1
        peak=1
        firstIndex=-1
        secondIndex=-1
        while i<j:
            mid=i+(j-i)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                i=mid+1
            else:
                j=mid
        peak=i
        #left half
        left=0
        right=peak
        while left<=right:
            mid=left+(right-left)//2
            if mountainArr.get(mid)==target:
                firstIndex=mid
                break
            elif mountainArr.get(mid)>target:
                right=mid-1
            else:
                left=mid+1
        #right half
        left=peak
        right=mountainArr.length()-1
        while left<=right:
            mid=left+(right-left)//2
            if mountainArr.get(mid)==target:
                secondIndex=mid
                break
            elif mountainArr.get(mid)<target:
                right=mid-1
            else:
                left=mid+1
        if firstIndex!=-1:
            return firstIndex
        elif secondIndex!=-1:
            return secondIndex
        return -1
            





        