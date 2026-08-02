# Time Complexity: O(1)
# Space Complexity: O(1)

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def peek(self) -> int:
        if not self.stack2:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

obj = MyQueue()
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())