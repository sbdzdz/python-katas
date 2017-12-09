from collections import defaultdict
import inputs
import re

class Node:
    def __init__(self, name, parent=None, children=None):
        self.weight = 0
        self.name = name
        self.parent = parent
        self.children = children

    def __repr__(self):
        return self.name + '–' + str(self.parent) + ': ' + str(self.children)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return NotImplemented


class Tree(dict):
    def __missing__(self, key):
        value = self[key] = Node(key)
        return value


def update(tree, parent, children):
    tree[parent].children = set(children)
    for child in children:
        tree[child].parent = parent
    return tree

def parse(line):
    pattern = re.compile(r'(.+) \((\d+)\) -> (.+)')
    match = re.match(pattern, line).groups()
    parent, children = match[0], match[2].split(', ') 
    return parent, children

tree = Tree()
for line in inputs.circus.split('\n'):
    if '->' in line:
        parent, children = parse(line)
        tree = update(tree, parent, children)

for node in tree:
    if tree[node].parent is None:
        print(node)
