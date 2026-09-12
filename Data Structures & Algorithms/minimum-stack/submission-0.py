class MinStack:
    """Two Stacks

    push/pop/top/getMin:  T = O(1)
    space: S = O(n)
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Each time a new element is pushed into the original stack,
        # the minimum element at that moment is pushed into a min stack
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        try:
            self.stack.pop()
            self.min_stack.pop()
        except IndexError:
            print("Pop from empty stack")

    def top(self) -> int:
        try:
            return self.stack[-1]
        except IndexError:
            print("Top from empty stack")
            return None

    def getMin(self) -> int:
        try:
            return self.min_stack[-1]
        except IndexError:
            print("Get min from empty stack")
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
