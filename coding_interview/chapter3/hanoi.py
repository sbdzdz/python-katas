from stack import Stack

class Tower(object):
    def __init__(self, number):
        self.stack = Stack()
        self.number = number 

    def push(self, value):
        self.stack.push(value)

    def peek(self):
        return self.stack.peek()

    def move(self, target):
        value = self.stack.pop()
        if value is not None and (target.peek() is None or target.peek() >= value):
            target.push(value)
            print(f'Move disk {value} from {self.number} to {target.number}')

    def move_n(self, n, aux, target):
        if n == 1:
            self.move(target)
        else:
            self.move_n(n-1, target, aux)
            self.move(target)
            aux.move_n(n-1, self, target)

num_towers = 3
num_disks = 4
towers = []
for i in range(num_towers):
    towers.append(Tower(i+1))
for i in range(1, num_disks+1):
    towers[0].push(i)
towers[0].move_n(num_disks, towers[1], towers[2])
