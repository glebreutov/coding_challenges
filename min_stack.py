class MinStack:

    def __init__(self):
        self.min_values = []
        self.stack_node = []

    def push(self, val: int) -> None:
        if self.min_values:
            mv = self.min_values[-1]
            self.min_values.append(min(mv, val))
        else:
            self.min_values.append(val)

        self.stack_node.append(val)

    def pop(self) -> None:
        self.min_values.pop()
        self.stack_node.pop()

    def top(self) -> int:
        return self.stack_node[-1]

    def getMin(self) -> int:
        return self.min_values[-1]