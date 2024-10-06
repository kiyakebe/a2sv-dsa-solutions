# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append([x, 0])

    def pop(self) -> int:
        if len(self.stack) > 1:
            self.stack[-2][1] += self.stack[-1][1]

        if self.stack:
            return sum(self.stack.pop())
        return -1

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        if k >= len(self.stack):
            self.stack[-1][1] += val
        else:
            self.stack[k-1][1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)