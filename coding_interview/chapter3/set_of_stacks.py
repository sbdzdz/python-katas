from stack import *

class SetOfStacks(object):
    def __init__(self, max_size):
        self.elements = 0
        self.max_size = max_size
        self.stacks = []

    def is_empty(self):
        return not self.stacks

    def pop(self):
        if self.stacks and not self.stacks[-1].is_empty():
            return self.stacks[-1].pop()
        if self.stacks and self.stacks[-1].is_empty():
            self.stacks.pop()
            return self.pop()

    def push(self, value):
        self.elements += 1
        if self.elements > self.max_size*len(self.stacks):
            self.stacks.append(Stack())
        self.stacks[-1].push(value)
