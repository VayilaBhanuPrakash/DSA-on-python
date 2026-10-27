class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        index = 0
        n = len(s)
        next = [0]
        farthest = 0
        while index < len(next):
            jump = next[index]
            index += 1
            start = max(jump + minJump, farthest + 1)
            end = min(jump + maxJump,n-1)
            for i in range(start,end + 1):
                if s[i] == '0':
                    next.append(i)
                    if i == n - 1:
                        return True
            farthest = max(farthest,end)
        return False

        

        