class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for ele in s:
            if ele.isalnum():
                st = st + ele.lower()
        i = 0
        j = len(st) - 1
        while i < j:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True
        