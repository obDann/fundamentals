from stack import *


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
        self.right = right


class BinarySearchTree():

    def __init__(self):
        '''
        (BinaryTree) -> None

        Initializes a Binary Search Tree where the value to the left of the
        tree is less than the root, and the value to the right of the tree
        is greater than or equal to the root
        '''
        # REPRESENTATION INVARIANT
        # _root is a BinaryNode at the very top of the tree or it is None
        # for any node m in the tree:
        #     m.left[.left|.right]* < m.data
        #     m.right[.left|.right] >= m.data

        # just initialize the root Node
        self._root = None

    def add(self, value):
        '''
        (BinaryTree, int) -> None

        Adds a value to the tree
        '''
        # we check if there is even a root node
        if (not self._root):
            # if there isnt, we set our root to be a new node
            self._root = BinaryNode(value)
        else:
            # otherwise, we can just call our helper function
            BinarySearchTree._add_helper(self._root, value)

    def remove(self, value):
        '''
        (BinaryTree, int) -> None

        Removes the first instance of the passed value in the BinarySearchTree
        through a pre-order traversal.
        '''
        # first, we want to check if this tree has a root
        if (self._root):
            # if it does, then we can find the path to the passed value
            stk, found = BinarySearchTree._get_path_to_obj(self._root,
                                                           value)
            # we get the node to remove
            removing_node = stk.pop()
            # check if there is a right child
            if (removing_node.right):
                # one case to consider is if the removing node does not have
                # a left node
                if (not removing_node.left):
                    # then we would have to split this into two cases
                    # case 1: check if there isn't parent by checking the stack
                    if (stk.is_empty()):
                        # in this case, we set the root node to be the right
                        # child
                        self._root = removing_node.right
                    # case 2: the removing node is an arbitrary node
                    else:
                        # in this case, we want to just get the parent
                        parent = stk.pop()
                        # determine where the child is
                        if (removing_node.data >= parent.data):
                            # then remove appropriately
                            parent.right = removing_node.right
                        else:
                            parent.left = removing_node.right
                else:
                    # suppose the removing node does have a left node
                    # which calls for replacement

                    # in this case, we want to get the right subtree's most
                    # left nodes of the node we want to remove
                    extreme, par_extr = self._abs_left(removing_node.right)

                    # we don't know if the removing node's right has a left
                    # node, so we check
                    if (removing_node.right.left):
                        # in this case, the node we want to remove is going to
                        # have its data overrwritten by the extreme leftward
                        # node
                        removing_node.data = extreme.data
                        # then we remove the extreme node by letting the
                        # parent of the extreme node's left pointer to be the
                        # right pointer of the extreme node
                        par_extr.left = extreme.right
                    else:
                        # if the removing node's right node does not have a
                        # left node, this varies on whether there is a parent
                        # or not

                        # in both cases, we set the right node's left pointer
                        # to become the left subtree of the removing node
                        removing_node.right.left = removing_node.left

                        # so we check if the node we want to remove is the root
                        if (stk.is_empty()):
                            # then we set the root to be the right node
                            self._root = removing_node.right
                        else:
                            # otherwise, we get the parent, and set it to
                            parent = stk.pop()
                            # determine where the child is
                            if (removing_node.data >= parent.data):
                                # then remove appropriately
                                parent.right = removing_node.right
                            else:
                                parent.left = removing_node.right
            elif (removing_node.left):
                # otherwise, we can assume that there is only a left tree
                # we have two cases
                # case 1: the node we want to remove is the root
                if (stk.is_empty()):
                    # if it is the root, we just set the root to become
                    # the next left node
                    self._root = removing_node.left

                # otherwise, it is an internal node
                else:
                    # so we get the parent
                    parent = stk.pop()
                    # determine where the child is
                    if (removing_node.data >= parent.data):
                        # then remove appropriately
                        parent.right = removing_node.left
                    else:
                        parent.left = removing_node.left
            else:
                # otherwise, if there isnt a left or a right, we would have
                # to remove the leaf

                # in this case, we check if the node we want to remove is the
                # root
                if (stk.is_empty()):
                    # if it is, then we set the root to be None
                    self._root = None
                # otherwise
                else:
                    # we get the parent
                    parent = stk.pop()
                    # determine where the child is
                    if (removing_node.data >= parent.data):
                        # then remove appropriately
                        parent.right = None
                    else:
                        parent.left = None

    @staticmethod
    def _abs_left(root):
        '''
        (BinaryNode) -> BinaryNode, BinaryNode

        Returns the most left two nodes from the passed root (the first
        node being the actual node before None)
        '''
        # make a crawler and a tagger
        crawler = root
        tagger = root

        # check if there is a left node
        while (crawler.left):
            # if there is, the tagger is going to be the crawler
            tagger = crawler
            # and the crawler traverses
            crawler = crawler.left

        return crawler, tagger

    def preorder_traversal_str(self):
        '''
        (BinaryTree) -> String

        Returns a string representation of a preorder traversal (VLR) in the
        BinaryTree
        '''
        # just call our helper function
        return BinarySearchTree._preorder_helper(self._root)

    def inorder_traversal_str(self):
        '''
        (BinaryTree) -> String

        Returns a string representation of an inorder traversal (LVR) in the
        BinaryTree
        '''
        # just call our helper function
        return BinarySearchTree._inorder_helper(self._root)

    def postorder_traversal_str(self):
        '''
        (BinaryTree) -> String

        Returns a string representation of a postorder traversal (LRV) in the
        BinaryTree
        '''
        # just call our helper function
        return BinarySearchTree._postorder_helper(self._root)

    @staticmethod
    def _preorder_helper(curr_node):
        '''
        (BinaryNode) -> String

        Returns the string representation of a preorder traversal
        '''
        # create a returning string
        ret = ""

        # check if our current node is not None
        if (curr_node):
            # our value is the current node
            ret = str(curr_node.data)
            # check if there is a left child
            if (curr_node.left):
                # if there is, we recursively call our preorder helper
                # towards the left child
                ret += " " + BinarySearchTree._preorder_helper(curr_node.left)
            # then check if there is a right child
            if (curr_node.right):
                # if there is, recrusively call our preorder helper towards
                # the right child
                ret += " " + BinarySearchTree._preorder_helper(curr_node.right)
        # then we just return our string
        return ret

    @staticmethod
    def _inorder_helper(curr_node):
        '''
        (BinaryNode) -> String

        Returns a string representation of an inorder traversal
        '''
        # create a returning string
        ret = ""

        # check if our current node is not None
        if (curr_node):
            # check if there is a left child
            if (curr_node.left):
                # if there is, we recursively call our inorder helper
                # towards the left child
                ret = BinarySearchTree._inorder_helper(curr_node.left) + " "
            # then add the current node's data
            ret += str(curr_node.data)
            # then check if there is a right child
            if (curr_node.right):
                # if there is, recrusively call our inorder helper towards
                # the right child
                ret += " " + BinarySearchTree._inorder_helper(curr_node.right)
        # then we just return our string
        return ret

    @staticmethod
    def _postorder_helper(curr_node):
        '''
        (BinaryNode) -> String
        Returns a string representation of a postorder traverse
        '''
        # create a returning string
        ret = ""

        # check if our current node is not None
        if (curr_node):
            # check if there is a left child
            if (curr_node.left):
                # if there is, we recusrively call our postorder helper
                # towards the left child
                ret = BinarySearchTree._postorder_helper(curr_node.left) + " "
            # then check if there is a right child
            if (curr_node.right):
                # if there is, we recursively call our postorder helper
                # towards the right child
                ret += BinarySearchTree._postorder_helper(curr_node.right)
                ret += " "
            # then add our data
            ret += str(curr_node.data)
        # then return our string
        return ret

    @staticmethod
    def _add_helper(curr, val):
        '''
        (BinaryNode, int) -> None

        Adds an object to the tree while maintaining the BST property, assuming
        that curr is not None
        '''
        # check if the passed value is greater than or equal to the
        # current node's data
        if (val >= curr.data):
            # if it is, then check if there isn't a right node
            if (not curr.right):
                # if there isn't we can make a node
                new_node = BinaryNode(val)
                # then have the current right node point to the new node
                curr.right = new_node
            else:
                # otherwise, we recursively call our helper towards the right
                BinarySearchTree._add_helper(curr.right, val)
        # otherwise, we can safely assume that the value is less than the
        # current node's data
        else:
            # we check if there isn't a left node
            if (not curr.left):
                # if there isn't, we can make a new node
                new_node = BinaryNode(val)
                # then have the current left node point to the new node
                curr.left = new_node
            else:
                # otherwise, we recursively call our helper towards the left
                BinarySearchTree._add_helper(curr.left, val)

    @staticmethod
    def _get_path_to_obj(curr_node, passed_val, stk=Stack()):
        '''
        (BinaryNode, int, Stack, BinaryNode) -> BinaryNode, boolean

        Returns a Stack trace from the passed value to the current node, and
        a boolean to indicate if the passed value is found in the tree

        If the value is not found it will return an empty stack

        REQ: the current node is not a NoneType
        '''
        # first check if the node is found with the current node
        found = curr_node.data == passed_val
        # if it is found, then we can just add that to our stack
        if (found):
            stk.push(curr_node)

        # otherwise, it is not found; we check if there is a left child
        if (curr_node.left and not found):
            # if there is a left node, add the current node
            stk.push(curr_node)
            # then recurse towards the left node
            stk, found = BinarySearchTree._get_path_to_obj(curr_node.left,
                                                           passed_val,
                                                           stk)
            # we check if the node is not found
            if (not found):
                # if it isn't, then we would like to revert back to
                # the parent of this node, so we peek
                recent = stk.peek()
                # then keep on popping until we find this node
                while (recent.data != curr_node.data):
                    stk.pop()
                    recent = stk.peek
                # then we pop this node
                stk.pop()

        # then we check the right child
        if (curr_node.right and not found):
            # if there is a right node, add the current node
            stk.push(curr_node)
            # then recurse towards the right node
            stk, found = BinarySearchTree._get_path_to_obj(curr_node.right,
                                                           passed_val,
                                                           stk)
            # we check if the node is not found
            if (not found):
                # if it isn't, then we would like to revert back to
                # the parent of this node, so we peek
                recent = stk.peek()
                # then keep on popping until we find this node
                while (recent.data != curr_node.data):
                    stk.pop()
                    recent = stk.peek
                # then we pop this node
                stk.pop()

        # then return our result
        return stk, found

if __name__ == '__main__':
    # ###########################################
    # test_remove_one_element
    # ##########################################
    one_ele_bst = BinarySearchTree()
    one_ele_bst.add(7)
    one_ele_bst.remove(7)
    expected = ""
    actual = one_ele_bst.preorder_traversal_str()
    if (actual == expected):
        print("test_remove_one_element successful")
    # ###########################################
    # test_remove_root_left_tree
    # ##########################################
    lt_root_test = BinarySearchTree()
    # add a few elements to make a left tree
    lt_root_test.add(10)
    lt_root_test.add(9)
    lt_root_test.add(8)
    lt_root_test.add(7)
    # remove the root
    lt_root_test.remove(10)

    # we expect the tree's preorder to be as follows
    expected = "9 8 7"
    actual = lt_root_test.preorder_traversal_str()
    if (actual == expected):
        print("test_remove_root_left_tree successful")

    # ###########################################
    # test_remove_root_right_tree
    # ##########################################
    rt_root_test = BinarySearchTree()
    # add a few elements to make a left tree
    rt_root_test.add(10)
    rt_root_test.add(20)
    rt_root_test.add(30)
    rt_root_test.add(52)
    # remove the root
    rt_root_test.remove(10)

    # we expect the tree's preorder to be as follows
    expected = "20 30 52"
    actual = rt_root_test.preorder_traversal_str()
    if (actual == expected):
        print("test_remove_root_right_tree successful")
