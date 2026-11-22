class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        chances = 1
        flag1 = True
        flag2 = True
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif chances:
                left += 1
                chances -= 1
            else:
                flag1 = False
                break
        left = 0
        right = len(s) - 1
        chances = 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif chances:
                right -= 1
                chances -= 1
            else:
                flag2 = False
                break
        return flag1 or flag2


        