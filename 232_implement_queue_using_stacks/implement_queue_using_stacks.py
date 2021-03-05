class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.out = Stack()
        self.inp = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inp.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.out) == 0:
            while len(self.inp) > 0:
                self.out.push(self.inp.pop())
        return self.out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.out) == 0:
            while len(self.inp) > 0:
                self.out.push(self.inp.pop())
        return self.out.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.inp) + len(self.out) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()