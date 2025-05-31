class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        toPop = self.stack[-1]
        self.stack = self.stack[:-1]
        return toPop 
    def top(self) -> int:
        return self.stack[-1]
    def empty(self) -> bool:
        return len(self.stack) == 0