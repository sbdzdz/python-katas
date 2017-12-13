import inputs

class StreamProcessor():
    def __init__(self):
        self.garbage = False
        self.total_score = 0
        self.group_counter = 0
        self.garbage_counter = 0

    def record(self, char):
        if c in '{}' and not self.garbage:
             self.group_processor(char)
        else:
            self.garbage_processor(char)

    def group_processor(self, char):
        if char == '{':
            self.group_counter += 1
        if char == '}':
            self.total_score += self.group_counter
            self.group_counter -= 1

    def garbage_processor(self, char):
        if char == '>':
            self.garbage = False
        if self.garbage:
            self.garbage_counter += 1
        if char == '<':
            self.garbage = True


p = StreamProcessor()
ignore = False
for c in inputs.stream:
    if ignore:
        ignore = False
        continue
    elif c == '!':
        ignore = True
    else:
        p.record(c)
print(p.total_score)
print(p.garbage_counter)
