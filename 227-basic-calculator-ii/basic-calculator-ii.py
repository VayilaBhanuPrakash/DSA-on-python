class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        operators = []

        num = 0
        for ele in s:
            if ele == " ":
                continue
            if ele.isdigit():
                num = num * 10 + (ord(ele) - ord('0'))
            else:
                nums.append(num)
                operators.append(ele)
                num = 0
        nums.append(num)

        i = 0
        while i < len(operators):
            if operators[i] == "*" or operators[i] == "/":
                a = nums[i]
                b = nums[i + 1]
                val = a * b if operators[i] == "*" else a // b

                nums[i] = val
                del nums[i + 1]
                del operators[i]
            else:
                i += 1
        

        res = nums[0]

        for i in range(len(operators)):
            res = res + nums[i + 1] if operators[i] == "+" else res - nums[i + 1]
        
        return res

        
            

            
        