class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        romans = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        res = ""
        n = len(romans) - 1
        while num > 0:
            for i in range(n,-1,-1):
                if values[i] > num:
                    continue
                else:
                    res = res + romans[i]
                    num = num - values[i]
                    n = i
                    break
        return res

        
