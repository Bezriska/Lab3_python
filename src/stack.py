class Stack:

    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("Выталкивание из пустого стека")

        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        a = self.stack.pop()
        return a

    def push(self, x: int) -> None:
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

        self.stack.append(x)

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self) -> int:
        if not self.stack:
            raise IndexError(
                "Невозможно узнать верхнее значение, т.к. стек пуст")

        top = self.stack[-1]
        return top

    def __len___(self) -> int:
        res = 0

        for _ in self.stack:
            res += 1

        return res

    def min(self) -> int:
        return self.min_stack[-1]
