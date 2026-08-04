class MyStack:
    def __init__(self):
        self.storage = []
    
    def push(self , x:int) -> None:
        self.storage.append(x)
        return None
        
    def pop(self) -> int:
        if len(self.storage) != 0:
            return self.storage.pop(-1)
        return None

    def top(self) -> int:
        if len(self.storage) != 0:
            return self.storage[-1]
        return None

    def is_empty(self) -> bool:
        return len(self.storage) == 0
    
    def size(self) -> int:
        return len(self.storage) 

class MyQueue:

    def __init__(self):
        self.inStack = MyStack()
        self.outStack = MyStack()
        

    def push(self, x: int) -> None:
        self.inStack.push(x)
        return None
        

    def pop(self) -> int:
        if self.outStack.size() == 0:
            while self.inStack.size() > 0:
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

        

    def peek(self) -> int:
        if self.outStack.size() == 0:
            while self.inStack.size() > 0:
                self.outStack.push(self.inStack.pop())
        return self.outStack.top()
        

    def empty(self) -> bool:
        print(self.inStack.size())
        print(self.outStack.size())
        return self.inStack.size() == 0 and self.outStack.size() == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()