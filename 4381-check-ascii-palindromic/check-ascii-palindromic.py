class Solution:
    def isPalindromic(self, s: str) -> bool:
        bs = ""
        for ele in s:
            val = ord(ele)
            b = ""
            while val != 0:
                rem = val % 2
                b = str(rem) + b
                val = val //2
            while len(b) < 8:
                b = str('0') + b
            bs = bs + b

        i = 0
        j = len(bs) - 1
        while i <= j:
            if bs[i] != bs[j]:
                return False
            i += 1
            j -= 1
        return True
        