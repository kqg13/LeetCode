# 155: Min Stack
# https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150


class MinStack:
    def __init__(self):
        self.core_stack = []
        self.max_val = (2 ** 31) - 1
        self.min_stack = [self.max_val + 1]

    def push(self, val: int) -> None:
        self.core_stack.append(val)
        if val <= self.getMin():
            self.min_stack.append(val)

    def pop(self) -> None:
        top_ele = self.core_stack.pop()
        if top_ele <= self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        return self.core_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()  # return -3
minStack.pop()
minStack.top()  # return 0
minStack.getMin()  # return -2
