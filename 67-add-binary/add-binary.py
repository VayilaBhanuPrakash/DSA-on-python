class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = -1
        carry = 0
        while i >= -len(a) and i >= -len(b):
            count = carry
            if a[i] == '1':
                count += 1
            if b[i] == '1':
                count += 1
            if count == 0:
                res.append('0')
            elif count == 1:
                res.append('1')
                carry = 0
            elif count == 2:
                res.append('0')
                carry = 1
            else:
                res.append('1')
                carry = 1
            i -= 1
            
        while i >= -len(a):
            count = carry
            if a[i] == '1':
                count += 1
            if count == 0:
                res.append('0')
            elif count == 1:
                res.append('1')
                carry = 0
            elif count == 2:
                res.append('0')
                carry = 1
            i -= 1

        while i >= -len(b):
            count = carry
            if b[i] == '1':
                count += 1
            if count == 0:
                res.append('0')
            elif count == 1:
                res.append('1')
                carry = 0
            elif count == 2:
                res.append('0')
                carry = 1
            i -= 1

        if carry:
            res.append('1')

        res.reverse()

        return ''.join(res)
        
            


        