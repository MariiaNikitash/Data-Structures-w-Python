class MinStack:

    def __init__(self):
        self.vals = []
        self.mins = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        # if mins empty or val that im pushing
        # is less then the current min
        # then I have a new min
        if not self.mins or val < self.mins[-1]:
            # append new min
            self.mins.append(val)
        else:
            # append the same min again
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.mins.pop()
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

owen = MinStack()
owen.push(2)
owen.push(12)
owen.push(1)
owen.push(4)
owen.push(2)
owen.push(-4)

#owen.pop()
print(owen.getMin())