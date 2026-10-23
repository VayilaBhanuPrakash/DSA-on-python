class Solution:
    def pivotInteger(self, n: int) -> int:
        i = 1
        j = n
        start = 0
        end = 0
        while i < j:
            if start == end:
                start += i
                end += j
                i += 1
                j -= 1
            elif start < end:
                start += i
                i += 1
            else:
                end += j
                j -= 1
        if start == end:
            return i
        return -1

        