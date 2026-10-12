class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        h = {}
        for ele in words2:
            h1 = {}
            for letter in ele:
                if letter not in h1:
                    h1[letter] = 1
                else:
                    h1[letter] += 1
            for keys in h1:
                if keys not in h:
                    h[keys] = h1[keys]
                else:
                    h[keys] = max(h[keys],h1[keys])
                
        res = []
        for ele in words1:
            h2 = {}
            for letter in ele:
                if letter not in h2:
                    h2[letter] = 1
                else:
                    h2[letter] += 1
            for keys in h:
                if keys not in h2:
                    break
                elif h[keys] > h2[keys]:
                    break
            else:
                res.append(ele)
        return res
        