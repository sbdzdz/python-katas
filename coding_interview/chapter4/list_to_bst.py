from tree import *

def list_to_bst(l):
    if not l:
        return None
    elif len(l) == 1:
        return TreeNode(l[0])
    else:
        middle = len(l)//2
        root = TreeNode(l[middle])
        root.left = list_to_bst(l[:middle])
        root.right = list_to_bst(l[middle+1:])
    return root
