class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        l = sentence.split(" ")
        for i in range(len(l)):
            if len(l[i]) > 1 and l[i][0] == "$" and l[i][1:].isdigit():
                l[i] = l[i][0] + str(f"{int(l[i][1:]) * ((100 - discount) / 100):.2f}")
        return " ".join(l)

        