class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 12:
            return -1
        
        l = []
        temp = n
        while n:
            rem = n % 10
            l.append(rem)
            n = n // 10
        l = l[::-1]

        n = len(l)
        if n == 2:
            l.sort()
            if l[1]  * 10 + l[0] == temp:
                return -1
            return l[1]  * 10 + l[0]
        
        i = n - 1
        list = [l[i]]
        i -= 1
        while i >= 0:
            if l[i] < max(list):
                break
            list.append(l[i])
            i -= 1
        if i < 0:
            return -1

        res = []
        for j in range(i):
            res.append(l[j])
            
        val = l[i]
        temp = l[i+1:]
        temp.sort()
        i = 0
        for i in range(len(temp)):
            if temp[i] > val:
                temp_val = val
                val = temp[i]
                temp[i] = temp_val
                break
        res.append(val)
        res.extend(temp)

        result = 0
        for ele in res:
            result = result * 10 + ele
        if result > 2 ** 31 - 1:
            return -1
        return result
        