"""
@Harsha
Date : 21/3/18
"""


class BSTNode(object):
    """
    Class defining individual properties of each node
    """

    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val


class BST(BSTNode):
    """
    Base class defining all operations wrt to each tree structure
    """

    def __init__(self):
        self.root = None

    def insert(self, val):
        node = BSTNode(val)
        if self.root is None:
            self.root = node
            print("Root inserted with ", val)
        else:
            current_node = self.root
            while True:
                if val < current_node.val:
                    print("Left tree traversal")
                    if current_node.left is None:
                        print("No left child")
                        node.parent = current_node
                        current_node.left = node
                        break
                    else:
                        current_node = current_node.left
                else:
                    print("Right tree traversal")
                    if current_node.right is None:
                        print("No Right child")
                        node.parent = current_node
                        current_node.right = node
                        break
                    else:
                        current_node = current_node.right

    def delete(self, val):
        pass

    def find_min(self):
        node = self.root
        if node is not None:
            while node.left is not None:
                node = node.left
            return node.val
        else:
            return "No elements Present"

    def delete_min(self):
        node = self.root
        while node.left is not None:
            node = node.left
        if node == self.root:
            self.root = self.root.right
        elif node.right is None:
            node.parent.left = None
        else:
            node.parent.left = node.right


if __name__ == '__main__':
    bst = BST()
    bst.insert(2)
    bst.insert(32)
    bst.insert(312)
    bst.insert(9)
    bst.insert(1)
    min_val = bst.find_min()
    print(min_val)
