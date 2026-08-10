class StockSpanner:

    def __init__(self):
        self.stack = [] 

    def next(self, price: int) -> int:
        span = 1
    
        while self.stack and price >= self.stack[-1][1]:
            span += self.stack.pop()[0]
        self.stack.append((span, price))
        
        return span
