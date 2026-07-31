class Solution:
    def minimumPushes(self, word: str) -> int:
        h = {}
        for ele in word:
            if ele in h:
                h[ele] += 1
            else:
                h[ele] = 1
        l = []
        for values in h.values():
            l.append(values)
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

