class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix_xor = [0 for _ in arr]
        prefix_xor[0] = arr[0]
        for i in range(1,len(arr)):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]

        res = [0 for _ in queries]  
        for i in range(len(queries)):
            if queries[i][0] == 0:
                res[i] = prefix_xor[queries[i][1]]
            else:
                res[i] = prefix_xor[queries[i][1]] ^ prefix_xor[queries[i][0] - 1] 
                
        return res