class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, value):
        self.left = TreeNode(value)

    def add_right(self, value):
        self.right = TreeNode(value)
