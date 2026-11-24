class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        op = []
        num = 0

        for ele in s:
            if ele == " ":
                continue
            elif ele.isdigit():
                num = num * 10 + (ord(ele) - ord('0'))
            else:
                nums.append(num)
                op.append(ele)
                num = 0
        nums.append(num)
        
        i = 0
        while i < len(op):
            if op[i] == "*" or op[i] == "/":
                a = nums[i] 
                b = nums[i + 1]

                val = a * b if op[i] == "*" else a // b
                nums[i] = val
                del nums[i + 1]
                del op[i]
            else:
                i += 1
        res = nums[0]

        for i in range(len(op)):
            res = res + nums[i + 1] if op[i] == "+" else res - nums[i + 1]
        
        return res
        