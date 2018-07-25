from stack import Stack

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class NodeQueue(object):
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        if self.front is None:
            self.front = Node(value)
            self.back = self.front
        else:
            node = Node(value)
            self.back.next = node
            self.back = self.back.next

    def dequeue(self):
        if self.front is not None:
            value = self.front.value
            self.front = self.front.next
            return value 

class MyQueue(object):
    def __init__(self):
        self.dequeue_stack = Stack()
        self.enqueue_stack = Stack()

    def enqueue(self, value):
        if not self.dequeue_stack.is_empty():
            while not self.dequeue_stack.is_empty():
                self.enqueue_stack.push(self.dequeue_stack.pop())
        self.enqueue_stack.push(value)

    def dequeue(self):
        if not self.dequeue_stack.is_empty():
            return self.dequeue_stack.pop()
        elif not self.enqueue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()
