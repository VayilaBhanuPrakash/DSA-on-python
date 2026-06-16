class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        res = []
        for ele in arr:
            if ele == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(ele)
        for i in range(len(arr)):
            arr[i] = res[i]
        """
        Do not return anything, modify arr in-place instead.
        """
        