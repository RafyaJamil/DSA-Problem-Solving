# Time Complexity: O(1)
# Space Complexity: O(1)

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if(not self.minStack or value <= self.minStack[-1] ):
            self.minStack.append(value)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


obj = MinStack()
print(obj.push(3))
print(obj.push(-1))
print(obj.push(2))
print(obj.pop())
print(obj.top())
print(obj.getMin())