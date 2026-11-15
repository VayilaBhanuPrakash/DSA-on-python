class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0
        for ele in bills:
            if ele == 5:
                five += 1
            elif ele == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five > 0 and ten > 0:
                    ten -= 1
                    five -= 1 
                elif five > 2:
                    five -= 3
                else:
                    return False

        return True
            

        