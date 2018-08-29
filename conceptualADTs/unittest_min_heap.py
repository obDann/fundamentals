from min_heap import *
import unittest


class TestMinHeap(unittest.TestCase):

    def setUp(self):
        # create a min heap
        self.mh = MinHeap()

    def test_initialization(self):
        # check if the min heap is a min heap
        self.assertTrue(isinstance(self.mh, MinHeap))

    def test_empty_on_init(self):
        # check if the min heap is empty
        self.assertTrue(self.mh.is_empty())

    def test_remove_on_empty(self):
        # check if the min heap raises an exception
        self.assertRaises(HeapEmptyException, self.mh.remove_min)

    def test_non_empty(self):
        # add one object to the heap
        obj = 4
        self.mh.insert(obj)
        # then we want to ensure that it is non empty
        self.assertFalse(self.mh.is_empty())

    def test_add_obj_then_remove(self):
        # create an expected obj
        expected = 55
        # then add it
        self.mh.insert(expected)
        # remove it
        actual = self.mh.remove_min()

        # test if the objects are the same
        self.assertEqual(actual, expected)
        # and test if the heap is empty
        self.assertTrue(self.mh.is_empty())

    def test_add_several_obj_then_remove(self):
        expected_first = 55
        expected_second = 56
        expected_third = 57
        # add them
        self.mh.insert(expected_first)
        self.mh.insert(expected_second)
        self.mh.insert(expected_third)

        # ensure that it is not empty
        self.assertFalse(self.mh.is_empty())

        # then remove them
        actual_first = self.mh.remove_min()
        actual_second = self.mh.remove_min()
        actual_third = self.mh.remove_min()

        # ensure that the heap is empty
        self.assertTrue(self.mh.is_empty())

        # compare the objects we removed
        self.assertEqual(actual_first, expected_first)
        self.assertEqual(actual_second, expected_second)
        self.assertEqual(actual_third, expected_third)

    def test_add_sever_obj_not_queue(self):
        # insert several objects in a random order, but we create our obj
        first_obj = 33
        second_obj = 22
        third_obj = 500
        fourth_obj = 2
        fifth_obj = -3
        sixth_obj = 22

        # add the objects to the heap in a random order
        self.mh.insert(third_obj)
        self.mh.insert(first_obj)
        self.mh.insert(second_obj)
        self.mh.insert(fifth_obj)
        self.mh.insert(fourth_obj)
        self.mh.insert(second_obj)

        # so we get our objects
        actual_first = self.mh.remove_min()
        actual_second = self.mh.remove_min()
        actual_third = self.mh.remove_min()
        actual_fourth = self.mh.remove_min()
        actual_fifth = self.mh.remove_min()
        actual_sixth = self.mh.remove_min()

        # from highest to lowest, our order is:
        # -3 2 22 22 33 500
        # so we compare it
        self.assertEqual(actual_first, -3)
        self.assertEqual(actual_second, 2)
        self.assertEqual(actual_third, 22)
        self.assertEqual(actual_fourth, 22)
        self.assertEqual(actual_fifth, 33)
        self.assertEqual(actual_sixth, 500)

if __name__ == '__main__':
    unittest.main(exit=False)