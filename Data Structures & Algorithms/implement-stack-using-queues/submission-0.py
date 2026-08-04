class MyQueue:
    def __init__(self):
        self.storage = []
    
    def push(self , x: int) -> None:
        self.storage.append(x)
        return None
    
    def peek(self , last: bool) -> int:
        if len(self.storage) != 0:
            return self.storage[0] if not last else self.storage[-1] 
        return None
    
    def pop(self , last: bool) -> int:
        if len(self.storage) != 0:
            return self.storage.pop(0) if not last else self.storage.pop(-1)
        return None
    
    def size(self) -> int:
        return len(self.storage)
    
    def is_empty(self) -> bool:
        return len(self.storage) == 0
    


class MyStack:
    def __init__(self):
        self.queue = MyQueue()

    def push(self, x: int) -> None:
        self.queue.push(x)
        return None
        

    def pop(self) -> int:
        return self.queue.pop(True)
        

    def top(self) -> int:
        return self.queue.peek(True)
        

    def empty(self) -> bool:
        return self.queue.is_empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()