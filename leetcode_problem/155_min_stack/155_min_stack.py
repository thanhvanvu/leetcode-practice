# https://www.youtube.com/watch?v=qkLl7nAwDPo
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

        # idea for getMin
        # 1/ Create another stack called minStack
        # 2/ when "pushing" new value, check the "before" value with new "value" in the minStack
        # 3/ if "new" value < "before" value, "pushing" new value to minStack

    def push(self, val: int) -> None:
        self.stack.append(val)

        # check if minStack is empty?
        if self.minStack:
            beforeVal = self.minStack[-1]
        else:
            beforeVal = val  # only for 1st operation

        minVal = min(beforeVal, val)

        # push new min value into minStack
        self.minStack.append(minVal)

    def pop(self) -> None:

        # need to pop both stack and minStack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        topVal = self.stack[-1]
        return topVal

    def getMin(self) -> int:
        minVal = self.minStack[-1]
        return minVal
