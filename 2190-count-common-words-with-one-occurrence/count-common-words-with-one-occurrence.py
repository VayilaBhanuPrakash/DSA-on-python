class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        h1 = {}
        for ele in words1:
            if ele in h1:
                h1[ele] += 1
            else:
                h1[ele] = 1
        h2 = {}
        for ele in words2:
            if ele in h2:
                h2[ele] += 1
            else:
                h2[ele] = 1
        res = 0
        for ele in h1:
            if ele not in h2:
                continue
            elif h1[ele] == 1 and h2[ele] == 1:
                res += 1
        return res
        