class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def add(self, node, key):
        if node == None:
            node = Node(key)
            return
        if node.value < key:
            if node.right == None:
                node.right = Node(key)
                return
            else:
                self.add(node.right, key)
        else:
            if node.left == None:
                node.left = Node(key)
                return
            else:
                self.add(node.left, key)

    def insert(self, new_val):
        # Your code goes here
        if new_val == None:
            return
        self.add(self.root, new_val)

    def show(self, start):
        while start != None:
            print(start.value)
            return self.show(start.left)
            return self.show(start.right)

    def printSelf(self):
        # Your code goes here
        if self.root == None:
            return -1
        self.show(self.root)

    def find(self, start, key):
        if start.value == key:
            return True
        if start.value < key:
            return self.find(start.right, key)
        if start.value > key:
            return self.find(start.left, key)

    def search(self, find_val):
        # Your code goes here
        if find_val == None or type(find_val) != 'int':
            return False
        if self.find(self.root, find_val):
            return True
        return False


tree = BST(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print(tree.search(3))
