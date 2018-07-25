class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class MinStack(object):
    def __init__(self):
        self.top = None
        self.min = None

    def push(self, value):
        self.push_min(value)
        node = Node(value)
        node.next = self.top
        self.top = node

    def push_min(self, value):
        node = Node(value)
        if self.min is None:
            self.min = node 
        elif node.value <= self.min.value:
            node.next = self.min
            self.min = node

    def pop(self):
        if self.top is not None:
            value = self.top.value
            self.pop_min(value)
            self.top = self.top.next
            return value

    def pop_min(self, value):
        if value == self.min.value:
            self.min = self.min.next

    def get_min(self):
        if self.min is not None:
            return self.min.value

    def is_empty(self):
        return self.top is None
