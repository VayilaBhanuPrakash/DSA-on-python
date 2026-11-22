class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        def isPalindrome(s,i,j):
            left = i
            right = j
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s, left+ 1, right) or isPalindrome(s, left, right - 1)
        return True   
            


        