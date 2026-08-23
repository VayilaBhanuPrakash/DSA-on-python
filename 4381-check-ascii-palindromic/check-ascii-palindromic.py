class Solution:
    def isPalindromic(self, s: str) -> bool:
        bs = ""
        for ele in s:
            b = bin(ord(ele))
            bb = (8 - (len(b) - 2))*"0" + b[2:]
            bs = bs + bb

        return bs == bs[::-1]

        i = 0
        j = len(bs) - 1
        while i <= j:
            if bs[i] != bs[j]:
                return False
            i += 1
            j -= 1
        return True
        