class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new = ""
            for i in range(0, len(s), k):
                value = 0
                for ele in s[i : i + k]:
                    value += ord(ele) - 48
                temp = ""
                if not value:
                    temp = chr(value + 48)
                while value:
                    last = value % 10
                    temp += chr(last + 48)
                    value = value // 10
                new = new + temp[::-1]
                print(new)
            s = new
        return s

