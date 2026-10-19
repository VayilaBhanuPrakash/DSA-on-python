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
        i = n - 2
        li = [l[i + 1]]
        while i >= 0:
            if l[i] < max(li):
                break
            li.append(l[i])
            i -= 1
        if i < 0:
            return -1
        res = []
        for j in range(i):
            res.append(l[j])
        temp = l[i+1:]
        temp.sort()
        val = l[i]
        i = 0
        while i < len(temp):
            if temp[i] <= val:
                i += 1
            else:
                flag = val
                val = temp[i]
                temp[i] = flag
                break
        res.append(val)
        res.extend(temp)
        result = 0
        for ele in res:
            result = result * 10 + ele
        if result > 2 ** 31 - 1:
            return -1
        return result
        