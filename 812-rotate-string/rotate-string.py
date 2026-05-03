class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n1=len(s)
        n2=len(goal)
        if n1!=n2:
            return False

        for i in range(n1):
            s=s[1:]+s[0]
            if s==goal:
                return True
        return False
        