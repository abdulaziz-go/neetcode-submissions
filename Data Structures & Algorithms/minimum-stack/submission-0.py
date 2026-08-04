class MinStack:

    def __init__(self):
        self.MinStack = []
        self.Stack = []
        

    def push(self, val: int) -> None:
        self.Stack.append(val)

        if len(self.MinStack) == 0 or self.MinStack[-1] >= val:
            self.MinStack.append(val)
        return None
        

    def pop(self) -> None:
        number =  self.Stack.pop()
        if number == self.MinStack[-1]:
            self.MinStack.pop()
        return None
        

    def top(self) -> int:
        if len(self.Stack) != 0:
            return self.Stack[-1]
        

    def getMin(self) -> int:
        if len(self.MinStack) != 0:
            return self.MinStack[-1]
        
