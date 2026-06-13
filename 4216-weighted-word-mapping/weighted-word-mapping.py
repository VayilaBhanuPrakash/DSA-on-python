class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for strings in words:
            sum = 0
            for letters in strings:
                sum += weights[ord(letters) - 97]
            sum = sum % 26
            res += chr(122 - sum)
        return res


            


        