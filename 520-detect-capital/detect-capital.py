class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = 0
        small = 0
        for letters in word:
            if letters.islower():
                small += 1
            elif letters.isupper():
                capital += 1
        if small == len(word) or capital == len(word):
            return True
        elif word[0].isupper() and small == len(word) - 1:
            return True
        return False

        