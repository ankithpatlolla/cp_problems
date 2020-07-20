class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        if new_val == None:
            return
        if self.root == None:
            self.root = Node(new.val)
        temp = self.root
        while temp != None:
            if temp.value < new_val:
                temp = temp.right
            else:
                temp = temp.left
        temp = Node(new_val)
        # print(temp.value)

    def printSelf(self):
        # Your code goes here
        if self.root == None:
            return
        temp = self.root
        while temp != None:
            temp = temp.left
            if temp == None:
                return
            print(temp.value)
            if temp == None:
                return
            temp = temp.right

    def search(self, find_val):
        # Your code goes here
        if find_val == None or type(find_val) != 'int':
            return False

        if self.root.value == find_val:
            return True
        temp = self.root
        while temp:
            if temp.value == find_val:
                return True
            elif temp.value < find_val:
                temp = temp.right
            else:
                temp = temp.right
        return False


tree = BST(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print(tree.printSelf())
