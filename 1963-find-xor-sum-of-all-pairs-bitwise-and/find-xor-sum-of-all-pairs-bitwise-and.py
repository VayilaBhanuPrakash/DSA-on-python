class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        arr1xorsum=0
        arr2xorsum=0
        for ele in arr1:
            arr1xorsum=arr1xorsum^ele
        for ele in arr2:
            arr2xorsum=arr2xorsum^ele
        print(arr1xorsum)
        print(arr2xorsum)
        return arr1xorsum & arr2xorsum
        


        