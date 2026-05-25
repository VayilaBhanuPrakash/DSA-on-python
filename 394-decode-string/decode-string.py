class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        num = 0
        curr_str=""
        for ele in s:
            if ele.isdigit():
                num = num*10 + int(ele)
            elif ele.isalpha():
                curr_str = curr_str + ele
            elif ele == "[":
                stack.append((num,curr_str))
                num=0
                curr_str=""
            else:
                mul,prev_str = stack.pop()
                curr_str = prev_str + mul * curr_str
        return curr_str  




