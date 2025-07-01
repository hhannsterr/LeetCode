class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        if self.minimum is None:
            self.minimum = val
        else:
            self.minimum = min(self.minimum, val)
        self.stack.append((val, self.minimum))

    def pop(self) -> None:
        self.stack.pop()
        self.minimum = self.getMin()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()