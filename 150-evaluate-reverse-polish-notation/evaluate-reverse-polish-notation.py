class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for ele in tokens:
            if ele in "/*+-":
                b = stack.pop()
                a = stack.pop()
                if ele == "+":
                    stack.append(a + b)
                elif ele == "-":
                    stack.append(a - b)
                elif ele == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(ele))

                
        return stack[-1]
            
        