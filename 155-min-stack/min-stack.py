class MinStack:

    def __init__(self):
        self.stack = []
        self.Minstack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.Minstack)==0:
            self.Minstack.append(value)
        else:
            self.Minstack.append(min(value,self.Minstack[-1]))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.Minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.Minstack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()