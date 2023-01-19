class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2  =[]
        
    def push(self, x: int) -> None:
         self.stack1.append(x)

    def pop(self) -> int:
         if len(self.stack2):
            return self.stack2.pop()
         else:
                while len(self.stack1):
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2):
            curr = self.stack2.pop()
            self.stack2.append(curr)
            return curr
        else:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
            curr = self.stack2.pop()
            self.stack2.append(curr)
            return curr
        
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
