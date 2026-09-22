class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                n1 = ord(num1[i]) - 48
                n2 = ord(num2[j]) - 48

                p = n1 * n2

                last_first = i + j + 1
                last_second = i + j

                t = p + res[last_first]

                res[last_first] = t % 10
                res[last_second] += t // 10
        result = ""
        for ele in res:
            if ele == 0 and result == "":
                continue
            result = result + chr(ele + 48)
        return result


        