# Space Complexity: O(n)
# Time Complexities:
# push()  -> O(1)
# pop()   -> O(n)
# top()   -> O(n)
# empty() -> O(1)

from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if self.queue2:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue2:
            while(self.queue1 and len(self.queue1) != 1):
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()
        else:
            while(self.queue2 and len(self.queue2) != 1):
                self.queue1.append(self.queue2.popleft())
            return self.queue2.popleft()

    def top(self) -> int:
        if not self.queue2:
            while(self.queue1 and len(self.queue1) != 1):
                self.queue2.append(self.queue1.popleft())
            x = self.queue1[0]
            self.queue2.append(self.queue1.popleft())
            return x
        else:
            while(self.queue2 and len(self.queue2) != 1):
                self.queue1.append(self.queue2.popleft())
            x = self.queue2[0]
            self.queue1.append(self.queue2.popleft())
            return x

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2

s = MyStack()
print(s.push(2))
print(s.push(4))
print(s.push(6))
print(s.push(8))
print(s.pop())
print(s.top())
print(s.empty())