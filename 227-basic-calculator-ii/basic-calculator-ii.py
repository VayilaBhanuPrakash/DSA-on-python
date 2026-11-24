class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        num = 0

        for i in range(len(s) + 1):
            ch = "+" if i == len(s) else s[i]

            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))
            
            elif ch != " ":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack[-1] = stack[-1] * num
                else:
                    stack[-1] = int(stack[-1] / num)

                num = 0
                op = ch
        return sum(stack)
        