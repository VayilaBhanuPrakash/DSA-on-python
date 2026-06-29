class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for ele in patterns:
            if ele in word:
                res += 1
        return res
        