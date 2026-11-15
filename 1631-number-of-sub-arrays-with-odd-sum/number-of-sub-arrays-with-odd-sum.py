class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        even_count = 1
        odd_count = 0
        prefix = 0
        res = 0

        for ele in arr:
            prefix += ele
            if prefix & 1 == 1:
                odd_count += 1
                res += even_count
            else:
                even_count += 1
                res += odd_count
            #print(prefix ,"even - ",even_count,"odd - ",odd_count)
        return res  % 1000000007
        