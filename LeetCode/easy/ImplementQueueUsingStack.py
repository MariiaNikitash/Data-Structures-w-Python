class MyQueue:

    def __init__(self):
       self.stack = []
       self.secondStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if not self.secondStack:
            while self.stack: # while s1 is not empty, take the last elem  and push to stack 2
                self.secondStack.append(self.stack.pop())
        return self.secondStack.pop()

    def peek(self) -> int:
        if not self.secondStack:
            while self.stack: # while s1 is not empty, take the last elem  and push to stack 2
                self.secondStack.append(self.stack.pop())
        return self.secondStack[-1]

    def empty(self) -> bool:
        return not self.stack and not self.secondStack

            

    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()