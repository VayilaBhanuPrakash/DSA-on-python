class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        top = 0
        while i < len(arr)-1:
            if arr[i] < arr[i+1]:
                i += 1
                top = 1
            else:
                break
        if top == 0 or i == len(arr) - 1:
            return False
        while i < len(arr)-1:
            if arr[i]> arr[i+1]:
                i += 1
            else:
                return False
        if top == 1:
            return True
        return False




        