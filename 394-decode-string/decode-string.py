class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != "]":
                stack.append(s[i])
                i += 1
            st = ""
            while stack and stack[-1] != "[":
                st = stack.pop() + st
            if stack and stack[-1] == "[":
                stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            mul = 1 if num == "" else int(num)
            stack.append(st * mul)
            i += 1

        return "".join(stack)







