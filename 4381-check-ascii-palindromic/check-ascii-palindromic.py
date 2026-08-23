class Solution:
    def isPalindromic(self, s: str) -> bool:
        bs = ""
        for ch in s:
            b = format(ord(ch),'08b')
            bs = bs + b

        return bs == bs[::-1]

        i = 0
        j = len(bs) - 1
        while i <= j:
            if bs[i] != bs[j]:
                return False
            i += 1
            j -= 1
        return True
        