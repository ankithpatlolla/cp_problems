class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def add(self, root, val):
        if root == None:
            root = new_val
            return
        if root.value < val:
            return add(root.right, val)
        return self.add(root.left, val)

    def insert(self, new_val):
        # Your code goes here
        self.add(self.root, new_val)

    def printSelf(self):
        # Your code goes here
        pass

    def search(self, find_val):
        # Your code goes here
        pass
