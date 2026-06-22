class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h = {}
        for letters in text:
            if letters in h:
                h[letters] += 1
            else:
                h[letters] = 1
        if 'l' in h:
            h['l'] = h['l'] // 2
        if 'o' in h:
            h['o'] = h['o'] // 2
        res = float('inf')
        word = "balon"
        for letters in word:
            if letters not in h:
                return 0
            res = min(res,h[letters])
        return res
        