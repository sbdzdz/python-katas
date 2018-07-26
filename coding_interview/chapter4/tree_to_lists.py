class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        node = Node(value)
        current = self
        while current.next is not None:
            current = current.next
        current.next = node

def tree_to_lists(root):
    if root is None:
        return []
    lists = []
    fringe = [(root, 0)]
    while fringe:
        current, level = fringe.pop(0)
        if len(lists) == level:
            lists.append(Node(current.value))
        else:
            lists[level].append(current.value)
        if current.left is not None:
            fringe.append((current.left, level+1))
        if current.right is not None:
            fringe.append((current.right, level+1))
    return lists
