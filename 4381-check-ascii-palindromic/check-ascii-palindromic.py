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
            
            b = str('0'*(8 - len(b))) + b
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
        