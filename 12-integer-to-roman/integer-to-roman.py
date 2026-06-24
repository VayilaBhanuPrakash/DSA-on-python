class Solution:
    def intToRoman(self, num: int) -> str:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l=[]
        nums=str(num)
        n=len(nums)
        for i in range(len(nums)):
            val=int(nums[i])*(10**(n-1-i))
            l.append(val)
        res = ""
        for ele in l:
            n = ele
            r = ""
            while n != 0:
                if n >= 900:
                    r = r + "M"
                    n = n - 1000
                elif n >= 400:
                    r = r + "D"
                    n = n - 500
                elif n >= 90:
                    r = r + "C"
                    n = n - 100
                elif n >= 40:
                    r = r + "L"
                    n = n - 50
                elif n >= 9:
                    r = r + "X"
                    n = n - 10
                elif n >= 4:
                    r = r + "V"
                    n = n - 5
                elif n >= 1:
                    r = r + "I"
                    n = n - 1
                elif n > -4:
                    r = "I" + r
                    n = n + 1
                elif n > -40:
                    r = "X" + r
                    n = n + 10
                elif n > -400:
                    r = "C" + r
                    n = n + 100
            res = res + r
        return res
                

                



            

        