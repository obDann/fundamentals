from binary_search_tree import *
import unittest


class TestBSTContd(unittest.TestCase):

    def setUp(self):
        # create a binary search tree
        self.bst = BinarySearchTree()

    def test_remove_one_element(self):
        # add an element from an empty BST
        self.bst.add(7)
        # then remove it
        self.bst.remove(7)
        expected = ""
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_root_left_tree(self):
        # add a few elements to make a left tree
        self.bst.add(10)
        self.bst.add(9)
        self.bst.add(8)
        self.bst.add(7)
        # remove the root
        self.bst.remove(10)

        # we expect the tree's preorder to be as follows
        expected = "9 8 7"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_root_right_tree(self):
        # add a few elements to make a right tree
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(30)
        self.bst.add(52)

        # remove the root
        self.bst.remove(10)
        expected = "20 30 52"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
