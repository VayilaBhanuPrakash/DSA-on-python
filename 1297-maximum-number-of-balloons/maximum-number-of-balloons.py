class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h = {}
        for letters in text:
            if letters in h:
                h[letters] += 1
            else:
                h[letters] = 1
        res = float('inf')
        word = "balon"
        for letters in word:
            if letters not in h:
                return 0
            elif letters == 'l' or letters == 'o':
                res = min(res,h[letters]//2)
            else:
                res = min(res,h[letters])
        return res
        