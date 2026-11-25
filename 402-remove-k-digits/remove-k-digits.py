class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        stack = [num[0]]
        for i in range(1,len(num)):
            while stack and num[i] < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k > 0:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack[i] == "0":
            i +=1
        return "".join(stack[i : ]) if stack[i : ] else "0"
        