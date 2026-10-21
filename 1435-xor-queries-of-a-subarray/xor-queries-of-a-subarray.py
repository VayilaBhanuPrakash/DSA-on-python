class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix_xor = [0]
        for i in range(len(arr)):
            prefix_xor.append(prefix_xor[i] ^ arr[i])

        res = []  
        for left,right in queries:
            res.append(prefix_xor[right + 1] ^ prefix_xor[left])

        return res
        