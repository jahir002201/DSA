class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue Peek:", queue.peek())
print("Queue Dequeue:", queue.dequeue())
print("Queue Is Empty:", queue.is_empty())
