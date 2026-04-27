class Solution:
    def removeStars(self, s: str) -> str:
        l=[]
        for ch in s:
            if ch=="*":
                l.pop()
            else:
                l.append(ch)
        return "".join(l)
        