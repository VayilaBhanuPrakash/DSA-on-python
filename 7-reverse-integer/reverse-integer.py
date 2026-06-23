class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            temp = -x
        else:
            temp = x
        rev = 0
        while temp != 0:
            rem = temp % 10 
            temp = temp //10
            rev = rev * 10 + rem
        if x < 0:
            rev = -rev
        if rev > 2**31-1 or rev < -2**31:
            return 0
        return rev



        