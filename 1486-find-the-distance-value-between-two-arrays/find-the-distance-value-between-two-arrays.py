class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for ele in arr1:
            flag = True
            first = 0
            last = len(arr2) - 1
            while first <= last:
                mid = (first + last) // 2
                if abs(ele - arr2[mid]) <= d:
                    flag = False
                    break
                elif ele > arr2[mid]:
                    first = mid + 1
                else:
                    last = mid - 1
            if flag:
                res += 1
        return res
        
        
        