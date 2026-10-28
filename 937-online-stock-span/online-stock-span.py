class StockSpanner:

    def __init__(self):
        self.ss = []
        self.index = 0
        

    def next(self, price: int) -> int:
        while self.ss and self.ss[-1][0] <= price:
            self.ss.pop()
        self.ss.append([price,self.index])
        self.index += 1
        if len(self.ss) == 1:
            return self.index

        return self.index - self.ss[-2][-1] -1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)