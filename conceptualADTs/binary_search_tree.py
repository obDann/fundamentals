class BinaryNode():

    def __init__(self, data, left=None, right=None):
        '''
        (BSTNode, int, BSTNode, BSTNode) -> None

        Initializes a Binary Node
        '''
        # REPRESENTATION INVARIANT
        # data holds data within the node
        # left is a pointer to a BinaryNode or None
        # right is a pointer to a BinaryNode or None

        # just initialize our variables
        self.data = data
        self.left = left
        self.righ = right


class BinarySearchTree():

    def __init__(self):
        '''
        (BinaryTree) -> None

        Initializes a Binary Search Tree where the value to the left of the
        tree is less than the root, and the value to the right of the tree
        is greater than the root
        '''
        # REPRESENTATION INVARIANT
        # root is a BinaryNode at the very top of the tree or it is None
        # for any node m in the tree:
        #     m.left[.left|.right]* < m.data
        #     m.right[.left|.right] >= m.data

    def add(self, value):
        '''
        (BinaryTree, int) -> None

        Adds a value to the tree
        '''

    def remove(self, value):
        '''
        (BinaryTree, int) -> None

        Removes the first instance of the passed value in the BinarySearchTree
        through a pre-order traversal.
        '''

    def preorder_traversal_str(self):
        '''
        (BinaryTree) -> String

        Returns a string representation of a preorder traversal (VLR) in the
        BinaryTree
        '''

    def inorder_traversal_str(self):
        '''
        (BinaryTree) -> String

        Returns a string representation of an inorder traversal (LVR) in the
        BinaryTree
        '''

    def postorder_traversal_str(self):
        '''
        (BinaryTree) -> String

        Returns a string representation of a postorder traversal (LRV) in the
        BinaryTree
        '''
