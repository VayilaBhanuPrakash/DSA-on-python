class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        h={')':'(',']':'[','}':'{'}
        for ele in s:
            if ele=='(' or ele=='[' or ele=='{':
                res.append(ele)
            else:
                if len(res) and res[-1]==h[ele]:
                    res.pop()
                else:
                    return False
        return len(res)==0

        