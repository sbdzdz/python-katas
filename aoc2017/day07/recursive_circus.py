from collections import Counter
import re

class Node:
    def __init__(self, name, parent=None, children=None):
        self.weight = 0
        self.total_weight = 0 
        self.name = name
        self.parent = parent
        self.children = children


class Tree(dict):
    def __missing__(self, key):
        value = self[key] = Node(key)
        return value


def update(tree, parent, children, weight):
    tree[parent].weight = weight
    tree[parent].total_weight = weight
    if children:
        tree[parent].children = set(children)
        for child in children:
            tree[child].parent = parent
    return tree

def parse(line):
    parent, weight, *children = line.split()
    weight = int(weight[1:-1])
    children = [child.strip(',') for child in children[1:]]
    return parent, children, weight 

def is_leaf(node):
    return node.children is None

def find_root(tree):
    for name, node in tree.items():
        if node.parent is None:
            return name

def are_balanced(nodes):
    return len(set(node.total_weight for node in nodes)) == 1

def find_imbalanced(nodes):
    weights = {node.total_weight: node for node in nodes}
    counter = Counter(weights.keys())
    majority_weight = counter.most_common(2)[0][0]
    outlier_weight = counter.most_common(2)[1][0]
    outlier = weights[outlier_weight]
    return majority_weight - (outlier.total_weight-outlier.weight)

def balance(tree):
    for node in tree:
        if not is_leaf(tree[node]):
            children = [tree[child] for child in tree[node].children]
            if all(is_leaf(child) for child in children):
                if are_balanced(children):
                    # collapse one level
                    tree[node].total_weight += sum(child.total_weight for child in children)
                    tree[node].children = None
                else:
                    return find_imbalanced(children)
    return balance(tree)

tree = Tree()
with open('input') as f:
    for line in f:
        tree = update(tree, *parse(line))

print(find_root(tree))
print(balance(tree))
