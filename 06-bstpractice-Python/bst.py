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
            self.root = new.val
        temp = self.root
        while temp != None:
            if temp.value < new_val:
                temp = temp.right
            else:
                temp = temp.left
        temp = new_val

    def printSelf(self):
        # Your code goes here
        if self.root == None:
            return False
        temp = self.root
        while temp:
            temp = temp.left
            print(temp)
            temp = temp.right

    def search(self, find_val):
        # Your code goes here
        if find_val == None or type(find_val) != 'int':
            return False
        temp = self.root
        while temp:
            if temp.value == find_val:
                return True
            elif temp.value < find_val:
                temp = temp.right
            else:
                temp = temp.right
        return False
