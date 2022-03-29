class Node(object):
#"""Bianary Tree search"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        else:
            print("Not found")

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


#                1
#               /  \
#              2    3
#             /\   /\
#            4  5  6  7
#                     /\
#                    8  9
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.left = Node(8)
tree.root.right.right.right = Node(9)
n=tree.print_tree("preorder")
print(n[0:len(n)-1])
