class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                st = ""
                while stack and stack[-1] != "[":
                    st = stack.pop() + st
                
                if stack and stack[-1] == "[":
                    stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                mul = int(num) if num else 1
                
                stack.append(mul * st)
        return "".join(stack)





