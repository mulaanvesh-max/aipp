from collections import deque

class QueueOptimized:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        if not self.items:
            raise IndexError("peek from empty queue")
        return self.items[0]

    def __str__(self):
        return f"Queue: {list(self.items)}"
