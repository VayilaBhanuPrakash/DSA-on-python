class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num == 1 and sum < 10:
            return str(sum)
        if num < (sum // 9 + (1 if sum % 9 else 0)):
            return ""

        nine = sum // 9
        rem = sum % 9
        res = "9" * nine + (str(rem) if rem else "")     

        result = res + "0" * (num - len(res))
        
        return result 
        
        