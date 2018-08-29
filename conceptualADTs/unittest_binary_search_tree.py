from binary_search_tree import *
import unittest


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        # create a binary search tree
        self.bst = BinarySearchTree()

    def test_initialization(self):
        # test whether the binary search tree is a binary search tree
        self.assertTrue(isinstance(self.bst, BinarySearchTree))

    def test_add(self):
        # add the number 10 to the binary search tree
        self.bst.add(10)
        # then we can use any ordered traversal to check if 10 is in the
        # tree
        actual = self.bst.preorder_traversal_str()
        expected = "10"
        self.assertEqual(actual, expected)

    def test_add_two_preorder_left(self):
        # add the number 10 followed by the number 5 to the binary
        # search tree
        self.bst.add(10)
        self.bst.add(5)
        # by preorder (VLR), 10 should come before 5
        expected = "10 5"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_two_inorder_left(self):
        # add the number 10 followed by the number 5 to the binary
        # search tree
        self.bst.add(10)
        self.bst.add(5)
        # by inorder (LVR), 5 should come before 10
        expected = "5 10"
        actual = self.bst.inorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_two_postorder_left(self):
        # add the number 10 followed by the number 5 to the binary
        # search tree
        self.bst.add(10)
        self.bst.add(5)
        # by postorder (LRV), 5 should come before 10
        expected = "5 10"
        actual = self.bst.postorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_two_preorder_right(self):
        # add the number 10 followed by the number 20 to the binary
        # search tree
        self.bst.add(10)
        self.bst.add(20)
        # by preorder (VLR), 10 comes before 20
        expected = "10 20"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_two_inorder_right(self):
        # add the number 10 followed by the number 20 to the binary
        # search tree
        self.bst.add(10)
        self.bst.add(20)
        # by inorder (LVR), 10 comes before 20
        expected = "10 20"
        actual = self.bst.inorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_two_postorder_right(self):
        # add the number 10 followed by the number 20 to the binary
        # search tree
        self.bst.add(10)
        self.bst.add(20)
        # by post order (LRV), 20 comes before 10
        expected = "20 10"
        actual = self.bst.postorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_three_complete_tree_preorder(self):
        # add the number 10 followed by the numbers 20 and 5
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(5)
        # by preorder (VLR), 10 comes first, followed by 5 then 20
        expected = "10 5 20"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_three_complete_tree_inorder(self):
        # add the number 10 followed by the numbers 20 and 5
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(5)
        # by inorder (LVR), 5 comes first, followed by 10 then 20
        expected = "5 10 20"
        actual = self.bst.inorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_add_three_complete_tree_postorder(self):
        # add the number 10 followed by the numbers 20 and 5
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(5)
        # by post order (LRV), 5 comes first, followed by 20 then 10
        expected = "5 20 10"
        actual = self.bst.postorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_left_tree_preorder(self):
        # add the number 10 followed by the numbers 5 3 and 1
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(3)
        self.bst.add(1)
        # by preorder (VLR), the order goes as follows
        expected = "10 5 3 1"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_left_tree_inorder(self):
        # add the number 10 followed by the numbers 5 3 and 1
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(3)
        self.bst.add(1)
        # by inorder (LVR), the order goes as follows
        expected = "1 3 5 10"
        actual = self.bst.inorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_left_tree_postorder(self):
        # add the number 10 followed by the numbers 5 3 and 1
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(3)
        self.bst.add(1)
        # by postorder (LRV), the order goes as follows
        expected = "1 3 5 10"
        actual = self.bst.postorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_right_tree_preorder(self):
        # add the number 10 followed by the numbers 20 30 500
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(30)
        self.bst.add(500)
        # by preorder (VLR), the order goes as follows
        expected = "10 20 30 500"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_right_tree_inorder(self):
        # add the number 10 followed by the numbers 20 30 500
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(30)
        self.bst.add(500)
        # by inorder (LVR), the order goes as follows
        expected = "10 20 30 500"
        actual = self.bst.inorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_right_tree_postorder(self):
        # add the number 10 followed by the numbers 20 30 500
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(30)
        self.bst.add(500)
        # by postorder (LRV), the order goes as follows
        expected = "500 30 20 10"
        actual = self.bst.postorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_crazy_tree_preorder(self):
        # we want a tree similar to the following
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /   \
        #           6    8       14   19

        # Add them breadth-first
        self.bst.add(10)
        self.bst.add(7)
        self.bst.add(20)
        self.bst.add(5)
        self.bst.add(9)
        self.bst.add(15)
        self.bst.add(30)
        self.bst.add(6)
        self.bst.add(8)
        self.bst.add(14)
        self.bst.add(19)

        # by preorder (VLR), the order goes as follows
        expected = "10 7 5 6 9 8 20 15 14 19 30"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_crazy_tree_inorder(self):
        # we want a tree similar to the following
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /   \
        #           6    8       14   19

        # Add them breadth-first
        self.bst.add(10)
        self.bst.add(7)
        self.bst.add(20)
        self.bst.add(5)
        self.bst.add(9)
        self.bst.add(15)
        self.bst.add(30)
        self.bst.add(6)
        self.bst.add(8)
        self.bst.add(14)
        self.bst.add(19)

        # by inorder (LVR), the order goes as follows
        expected = "5 6 7 8 9 10 14 15 19 20 30"
        actual = self.bst.inorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_crazy_tree_postorder(self):
        # we want a tree similar to the following
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /   \
        #           6    8       14   19

        # Add them breadth-first
        self.bst.add(10)
        self.bst.add(7)
        self.bst.add(20)
        self.bst.add(5)
        self.bst.add(9)
        self.bst.add(15)
        self.bst.add(30)
        self.bst.add(6)
        self.bst.add(8)
        self.bst.add(14)
        self.bst.add(19)
        # by post order (LRV), the order goes as follows
        expected = "6 5 8 9 7 14 19 15 30 20 10"
        actual = self.bst.postorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_from_empty(self):
        # remove an element from an empty BST
        self.bst.remove(7)
        expected = ""
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_non_existant_element(self):
        # add an element from an empty BST
        self.bst.add(8)
        # then attempt to remove an element that is not in the BST
        self.bst.remove(7)
        expected = "8"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_internal_node_left_tree(self):
        # add a few elements to make a left tree
        self.bst.add(10)
        self.bst.add(9)
        self.bst.add(8)
        self.bst.add(7)

        # remove an internal node
        self.bst.remove(8)
        expected = "10 9 7"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_leaf_left_tree(self):
        # add a few elements to make a left tree
        self.bst.add(10)
        self.bst.add(9)
        self.bst.add(8)
        self.bst.add(7)

        # remove the leaf
        self.bst.remove(7)
        expected = "10 9 8"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_internal_node_right_tree(self):
        # add a few elements to make a right tree
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(30)
        self.bst.add(52)

        # remove an internal node
        self.bst.remove(30)
        expected = "10 20 52"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_leaf_right_tree(self):
        # add a few elements to make a right tree
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(30)
        self.bst.add(52)
        # remove a leaf
        self.bst.remove(52)
        expected = "10 20 30"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_root_crazy_tree(self):
        # we want a tree similar to the following
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /   \
        #           6    8       14   19

        # Add them breadth-first
        self.bst.add(10)
        self.bst.add(7)
        self.bst.add(20)
        self.bst.add(5)
        self.bst.add(9)
        self.bst.add(15)
        self.bst.add(30)
        self.bst.add(6)
        self.bst.add(8)
        self.bst.add(14)
        self.bst.add(19)

        # remove the root
        self.bst.remove(10)
        # then we expect our tree to look like:
        #                      14
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /           \
        #           6    8            19
        # preorder traversal: VLR
        expected = "14 7 5 6 9 8 20 15 19 30"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_internal_one_child_crazy_tree(self):
        # we want a tree similar to the following
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /   \
        #           6    8       14   19
        # Add them breadth-first
        self.bst.add(10)
        self.bst.add(7)
        self.bst.add(20)
        self.bst.add(5)
        self.bst.add(9)
        self.bst.add(15)
        self.bst.add(30)
        self.bst.add(6)
        self.bst.add(8)
        self.bst.add(14)
        self.bst.add(19)

        # remove an internal node where there is only one child
        self.bst.remove(9)
        # then we expect our tree to look like:
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         8       15       30
        #          \               /  \
        #           6             14  19
        # preorder traversal: VLR
        expected = "10 7 5 6 8 20 15 14 19 30"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_internal_two_children_crazy_tree(self):
        # we want a tree similar to the following
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /   \
        #           6    8       14   19
        # Add them breadth-first
        self.bst.add(10)
        self.bst.add(7)
        self.bst.add(20)
        self.bst.add(5)
        self.bst.add(9)
        self.bst.add(15)
        self.bst.add(30)
        self.bst.add(6)
        self.bst.add(8)
        self.bst.add(14)
        self.bst.add(19)

        # then we want to remove a node that has two children
        self.bst.remove(7)
        # then we expect our tree to look like:
        #                      10
        #                 /           \
        #              8                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \              /   \
        #           6           14   19
        expected = "10 8 5 6 9 20 15 14 19 30"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

    def test_remove_leaf_crazy_tree(self):
        # we want a tree similar to the following
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /   \
        #           6    8       14   19
        # Add them breadth-first
        self.bst.add(10)
        self.bst.add(7)
        self.bst.add(20)
        self.bst.add(5)
        self.bst.add(9)
        self.bst.add(15)
        self.bst.add(30)
        self.bst.add(6)
        self.bst.add(8)
        self.bst.add(14)
        self.bst.add(19)

        # we can now remove a leaf
        self.bst.remove(19)

        # we expect the tree to be the following:
        #                      10
        #                 /           \
        #              7                 20
        #           /     \           /     \
        #         5         9       15       30
        #          \      /       /
        #           6    8       14
        expected = "10 7 5 6 9 8 20 15 14 30"
        actual = self.bst.preorder_traversal_str()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
