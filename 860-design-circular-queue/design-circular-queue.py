class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * k
        self.index = 0
        

    def enQueue(self, value: int) -> bool:
        if self.index < self.k:
            self.queue[self.index] = value
            self.index += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.index > 0 and self.index <= self.k:
            self.queue[0] = -1
            i = 0
            j = 1
            while j < self.k and self.queue[j] > -1:
                self.queue[i],self.queue[j] = self.queue[j],self.queue[i]
                i += 1
                j += 1
            self.index -= 1
            return True
        return False
        

    def Front(self) -> int:
        return self.queue[0]
        

    def Rear(self) -> int:
        return self.queue[self.index - 1]
        

    def isEmpty(self) -> bool:
        return self.index == 0
        

    def isFull(self) -> bool:
        return self.index == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()