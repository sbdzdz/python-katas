import inputs
from itertools import count, islice

def delta():
    for index in count():
        yield [(-1)**(index)] * index

def distance():
    x, y = 0, 0
    for d in delta():
        for element in d:
            yield abs(x) + abs(y)
            x += element
        for element in d:
            yield abs(x) + abs(y)
            y += element

print(list(islice(distance(), inputs.spiral))[-1])
