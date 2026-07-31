class Solution:
    def minimumPushes(self, word: str) -> int:
        l = [word.count(chr(97 + i)) for i in range(26)]
        l.sort()
        res = 0
        for i in range(-1,-(len(l)+1),-1):
            if i >= -8:
                res += 1 * l[i]
            elif i >= -16:
                res += 2 * l[i]
            elif i >= -24:
                res += 3 * l[i]
            else:
                res += 4 * l[i]
        return res

