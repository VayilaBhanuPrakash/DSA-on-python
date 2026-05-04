class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if ele in "([{":
                stack.append(ele)
            else:
                if ele==")" and (len(stack)==0 or stack.pop()!="("):
                    return False
                if ele=="]" and (len(stack)==0 or stack.pop()!="["):
                    return False
                if ele=="}" and (len(stack)==0 or stack.pop()!="{"):
                    return False
        return len(stack)==0
        