class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        carry = 0
        l = []
        while l1 >= 0 and l2 >= 0:
            num = carry + ord(num1[l1]) - 48 + ord(num2[l2]) - 48
            l.append(num % 10)
            carry = num // 10
            l1 -= 1
            l2 -= 1
        while l1 >= 0:
            num = carry + ord(num1[l1]) - 48
            l.append(num % 10)
            carry = num // 10
            l1 -= 1
        while l2 >= 0:
            num = carry + ord(num2[l2]) - 48
            l.append(num % 10)
            carry = num // 10
            l2 -= 1
        if carry > 0:
            l.append(carry)
        s = ""
        for i in range(len(l)-1,-1,-1):
            s = s + chr(l[i] + 48)
        return s

        