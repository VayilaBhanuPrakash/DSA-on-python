class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = {}
        for i in range(len(arr)):
            h[i] = abs(x - arr[i])
        i = 0 
        j = len(arr) -1
        for _ in range(len(arr)-k):
            if h[i] > h[j]:
                arr[i] = "mark"
                i += 1
            else:
                arr[j] = "mark"
                j -= 1
        res = []
        for ele in arr:
            if ele != "mark":
                res.append(ele)
        return res
        




        