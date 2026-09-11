class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = []

        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if j == i:
                    continue
                for k in range(len(digits)):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0 and [digits[i],digits[j],digits[k]] not in res:
                        res.append([digits[i],digits[j],digits[k]])
        return len(res)
        