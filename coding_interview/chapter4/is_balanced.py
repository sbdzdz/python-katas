def is_balanced(root):
    return (max_depth(root) - min_depth(root)) <= 1

def max_depth(root):
    if root is None:
        return 0
    return 1+max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    if root is None:
        return 0
    return 1+min(min_depth(root.left), min_depth(root.right))

def is_balanced_lame(root):
    fringe = [(root, 0)]
    levels = []
    while fringe:
        current, level = fringe.pop(0)
        if current.left is not None:
            fringe.append((current.left, level+1))
        if current.right is not None:
            fringe.append((current.right, level+1))
        if current.right == None and current.left == None:
            levels.append(level)
    return (max(levels) - min(levels)) <= 1
