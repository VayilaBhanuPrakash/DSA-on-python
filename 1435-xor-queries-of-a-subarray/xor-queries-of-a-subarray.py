class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix_xor = [0 for _ in arr]
        prefix_xor[0] = arr[0]
        for i in range(1,len(arr)):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]

        res = []  
        for left,right in queries:
            if left == 0:
                res.append(prefix_xor[right])
            else:
                res.append(prefix_xor[right] ^ prefix_xor[left - 1])

        return res
        