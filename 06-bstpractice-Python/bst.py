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
            root = Node(val)
            return
        while True:
            if root.value < val:
                if root.right == None:
                    root.right = Node(val)
                    return
                else:
                    root = root.right
            elif root.value > val:
                if root.left == None:
                    root.left = Node(root)
                    return
                else:
                    root = root.left

    def insert(self, new_val):
        # Your code goes here
        self.add(self.root, new_val)

    def print_bst(self, root):
        if root == None:
            return
        print(root)
        return self.print_bst(root.left)
        return self.print_bst(root.right)

    def printSelf(self):
        # Your code goes here
        self.print_bst(self.root)

    def search(self, find_val):
        # Your code goes here
        if self.root == None or type(self.root.value) != type(find_val):
            return False
        temp = self.root
        while temp != None:
            if temp.value == find_val:
                return True
            if temp.value < find_val:
                temp = temp.right
            else:
                temp = temp.left
        return False
