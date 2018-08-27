from linked_list import *
import unittest


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # create a linked list
        self.ll = LinkedList()

    def test_ll_initialization(self):
        # test if the linked list is a linked list
        self.assertTrue(isinstance(self.ll, LinkedList))

    def test_ll_is_empty(self):
        # test if the linked list is empty on initialization
        self.assertTrue(self.ll.is_empty())

    def test_ll_str_empty(self):
        # create an expected string
        expected = "Linked list is empty!"
        # get the actual string
        actual = self.ll.__str__()
        # compare the two
        self.assertEqual(actual, expected)

    def test_ll_get_num_ele_empty(self):
        # create an expected number of elements
        expected = 0
        # get the actual number of elements
        actual = self.ll.get_num_elements()
        # compare the two
        self.assertEqual(actual, expected)

    def test_bad_index_insert_low_empty(self):
        # create a bad index
        bad_index = -1
        # create some kind of object
        obj = "Object!"
        # then check if the exception was raised on an insert call
        self.assertRaises(BoundaryException, self.ll.insert, obj, bad_index)

    def test_bad_index_remove_low_empty(self):
        # create a bad index
        bad_index = -1
        # then check if the exception was raised on a remove call
        self.assertRaises(BoundaryException, self.ll.remove, bad_index)

    def test_bad_index_get_low_empty(self):
        # create a bad index
        bad_index = -1
        # then check if the exception was raised on a remove call
        self.assertRaises(BoundaryException, self.ll.get, bad_index)

    def test_bad_index_insert_high_empty(self):
        # create a bad index
        bad_index = 10
        # create some kind of object
        obj = "Object!"
        # then check if the exception was raised on an insert call
        self.assertRaises(BoundaryException, self.ll.insert, obj, bad_index)

    def test_bad_index_remove_high_empty(self):
        # create a bad index
        bad_index = 20
        # then check if the exception was raised on a remove call
        self.assertRaises(BoundaryException, self.ll.remove, bad_index)

    def test_bad_index_get_high_empty(self):
        # create a bad index
        bad_index = 15
        # then check if the exception was raised on a remove call
        self.assertRaises(BoundaryException, self.ll.get, bad_index)

    def test_append_once(self):
        # create an object to append
        obj = "4!"
        # append that object to the linked list
        self.ll.append(obj)
        # create an expected output
        expected = "4!"
        # determine the number of elements
        expected_num_ele = 1

        # we will test by using get
        actual_first = self.ll.get(0)
        # and a string representation
        actual_second = self.ll.__str__()
        # and the number of elements
        actual_num_ele = self.ll.get_num_elements()

        # compare the actuals vs expected
        self.assertEqual(actual_first, expected)
        self.assertEqual(actual_second, expected)
        self.assertEqual(actual_num_ele, expected_num_ele)

        # and test if the linked list is empty
        self.assertFalse(self.ll.is_empty())

    def test_append_twice(self):
        # create two objects to append
        first_obj = 44
        second_obj = False

        # append the two objects to our linked list
        self.ll.append(first_obj)
        self.ll.append(second_obj)

        # create an expected string
        expected_str = "44 -> False"

        # get the number of elements
        expected_num_ele = 2

        # then get our actuals
        actual_first = self.ll.get(0)
        actual_second = self.ll.get(1)
        actual_str = self.ll.__str__()
        actual_num_ele = self.ll.get_num_elements()

        # compare objects
        self.assertEqual(actual_first, first_obj)
        self.assertEqual(actual_second, second_obj)
        self.assertEqual(actual_str, expected_str)
        self.assertEqual(actual_num_ele, expected_num_ele)

        # and test if the linked list is empty
        self.assertFalse(self.ll.is_empty())

    def test_prepend_once(self):
        # create an object to append
        obj = "4!"
        # prepend that object to the linked list
        self.ll.prepend(obj)
        # create an expected output
        expected = "4!"
        # determine the number of elements
        expected_num_ele = 1

        # we will test by using get
        actual_first = self.ll.get(0)
        # and a string representation
        actual_second = self.ll.__str__()
        # and the number of elements
        actual_num_ele = self.ll.get_num_elements()

        # compare the actuals vs expected
        self.assertEqual(actual_first, expected)
        self.assertEqual(actual_second, expected)
        self.assertEqual(actual_num_ele, expected_num_ele)

        # and test if the linked list is empty
        self.assertFalse(self.ll.is_empty())

    def test_prepend_twice(self):
        # create two objects to prepend
        first_obj = 44
        second_obj = False

        # prepend the two objects to our linked list
        self.ll.prepend(first_obj)
        self.ll.prepend(second_obj)

        # create an expected string
        expected_str = "False -> 44"

        # get the number of elements
        expected_num_ele = 2

        # then get our actuals
        actual_first = self.ll.get(0)
        actual_second = self.ll.get(1)
        actual_str = self.ll.__str__()
        actual_num_ele = self.ll.get_num_elements()

        # compare objects
        self.assertEqual(actual_first, second_obj)
        self.assertEqual(actual_second, first_obj)
        self.assertEqual(actual_str, expected_str)
        self.assertEqual(actual_num_ele, expected_num_ele)

        # and test if the linked list is empty
        self.assertFalse(self.ll.is_empty())

    def test_insert_raw(self):
        # create an object to insert
        obj = "unique"

        # then insert the object into our linked list
        self.ll.insert(obj, 0)

        # we can now expect that the linked list has 1 element
        expected_num_ele = 1

        # we can test by get, string, and number of elements
        actual_first = self.ll.get(0)
        actual_second = self.ll.__str__()
        actual_num_ele = self.ll.get_num_elements()

        # so we compare the three
        self.assertEqual(actual_first, obj)
        self.assertEqual(actual_second, obj)
        self.assertEqual(actual_num_ele, expected_num_ele)

        # and we can test if the linked list is not empty
        self.assertFalse(self.ll.is_empty())

    def test_insert_beginning(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        to_insert = "An obj"
        # insert an object to the beginning of the list
        self.ll.insert(to_insert, 0)

        # we expect that there are 5 elements
        expected_num_ele = 5
        # we can test by string
        expected_str = "An obj -> one -> 2 -> three -> False"

        # so test by string
        actual_str = self.ll.__str__()
        # test by get
        actual_obj = self.ll.get(0)
        # test by number of elements
        actual_num_ele = self.ll.get_num_elements()

        # compare
        self.assertEqual(actual_obj, to_insert)
        self.assertEqual(actual_num_ele, expected_num_ele)
        self.assertEqual(actual_str, expected_str)

    def test_insert_end(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        to_insert = "An obj"
        # insert an object to the end of the list
        self.ll.insert(to_insert, 4)

        # we expect that there are 5 elements
        expected_num_ele = 5
        # we can test by string
        expected_str = "one -> 2 -> three -> False -> An obj"

        # so test by string
        actual_str = self.ll.__str__()
        # test by get
        actual_obj = self.ll.get(4)
        # test by number of elements
        actual_num_ele = self.ll.get_num_elements()

        # compare
        self.assertEqual(actual_obj, to_insert)
        self.assertEqual(actual_num_ele, expected_num_ele)
        self.assertEqual(actual_str, expected_str)

    def test_insert_middle(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        to_insert = "An obj"
        # insert an object to the middle of the list
        self.ll.insert(to_insert, 2)

        # we expect that there are 5 elements
        expected_num_ele = 5
        # we can test by string
        expected_str = "one -> 2 -> An obj -> three -> False"

        # so test by string
        actual_str = self.ll.__str__()
        # test by get
        actual_obj = self.ll.get(2)
        # test by number of elements
        actual_num_ele = self.ll.get_num_elements()

        # compare
        self.assertEqual(actual_obj, to_insert)
        self.assertEqual(actual_num_ele, expected_num_ele)
        self.assertEqual(actual_str, expected_str)

    def test_bad_index_insert_not_empty_low(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        # create an object to insert
        to_insert = "object!"
        # then attempt to insert the object with a bad index
        bad_index = -3
        self.assertRaises(BoundaryException, self.ll.insert, to_insert,
                          bad_index)

    def test_bad_index_insert_not_empty_high(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        # create an object to insert
        to_insert = "object!"
        # then attempt to insert the object with a bad index
        bad_index = 22
        self.assertRaises(BoundaryException, self.ll.insert, to_insert,
                          bad_index)

    def test_remove_beginning(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        # remove the first object
        self.ll.remove(0)

        # we expect that there are three objects
        expected_num_objs = 3
        # create an expected string
        expected_string = "2 -> three -> False"

        # get the actual number of objects and the actual string
        actual_num_objs = self.ll.get_num_elements()
        actual_str = self.ll.__str__()

        # generate comparisons
        self.assertEqual(actual_num_objs, expected_num_objs)
        self.assertEqual(actual_str, expected_string)

    def test_remove_end(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        # remove the last object
        self.ll.remove(3)

        # we expect that there are three objects
        expected_num_objs = 3
        # create an expected string
        expected_string = "one -> 2 -> three"

        # get the actual number of objects and the actual string
        actual_num_objs = self.ll.get_num_elements()
        actual_str = self.ll.__str__()

        # generate comparisons
        self.assertEqual(actual_num_objs, expected_num_objs)
        self.assertEqual(actual_str, expected_string)

    def test_remove_mid(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        # remove the second object
        self.ll.remove(1)

        # we expect that there are three objects
        expected_num_objs = 3
        # create an expected string
        expected_string = "one -> three -> False"

        # get the actual number of objects and the actual string
        actual_num_objs = self.ll.get_num_elements()
        actual_str = self.ll.__str__()

        # generate comparisons
        self.assertEqual(actual_num_objs, expected_num_objs)
        self.assertEqual(actual_str, expected_string)

    def test_remove_to_empty(self):
        # it is sufficient to put one object in the linked list
        self.ll.append("one")

        # then we can remove the object
        self.ll.remove(0)

        # test if the linked list is empty
        self.assertTrue(self.ll.is_empty())

    def test_bad_index_remove_empty(self):
        self.assertRaises(BoundaryException, self.ll.remove, 0)

    def test_bad_index_remove_non_empty_low(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        self.assertRaises(BoundaryException, self.ll.remove, -1)

    def test_bad_index_remove_non_empty_high(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        self.assertRaises(BoundaryException, self.ll.remove, 4)

    def test_bad_index_get_non_empty_high(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        self.assertRaises(BoundaryException, self.ll.get, 4)

    def test_bad_index_get_non_empty_low(self):
        # put four objects into our linked list
        self.ll.append("one")
        self.ll.append(2)
        self.ll.append("three")
        self.ll.append(False)

        self.assertRaises(BoundaryException, self.ll.get, -1)

    def test_reverse_empty(self):
        self.ll.reverse()
        # test if the linked list is still empty
        self.assertTrue(self.ll.is_empty())

    def test_reverse_one_ele(self):
        obj = "Obj!"
        # put one object into our linked list
        self.ll.append(obj)
        # then reverse it
        self.ll.reverse()
        # we expect that there is still only one element in the linked list
        expected_num_ele = 1

        # get the object
        actual_obj = self.ll.get(0)
        # get the string representation
        actual_str = self.ll.__str__()
        # get the number of elements
        actual_num_ele = self.ll.get_num_elements()

        # now we can compare
        self.assertEqual(actual_obj, obj)
        self.assertEqual(actual_str, obj)
        self.assertEqual(actual_num_ele, expected_num_ele)

    def test_reverse_multiple(self):
        first_obj = "one"
        second_obj = 2
        third_obj = "three"
        fourth_obj = False

        # put four objects into our linked list
        self.ll.append(first_obj)
        self.ll.append(second_obj)
        self.ll.append(third_obj)
        self.ll.append(fourth_obj)
        # reverse our linked list
        self.ll.reverse()

        # we still expect that there are 4 elements
        expected_num_ele = 4
        # we make an expected string
        expected_str = "False -> three -> 2 -> one"

        # get the actual number of elements
        actual_num_ele = self.ll.get_num_elements()
        # get the string representation after reversing
        actual_str = self.ll.__str__()
        # and consequently, let's get the sequential elements
        actual_first = self.ll.get(0)
        actual_second = self.ll.get(1)
        actual_third = self.ll.get(2)
        actual_fourth = self.ll.get(3)

        # test the string representation and the number of elements
        self.assertEqual(actual_num_ele, expected_num_ele)
        self.assertEqual(actual_str, expected_str)

        # test symmetry
        self.assertEqual(actual_first, fourth_obj)
        self.assertEqual(actual_second, third_obj)
        self.assertEqual(actual_third, second_obj)
        self.assertEqual(actual_fourth, first_obj)

    def test_append_after_reverse(self):
        first_obj = "one"
        second_obj = 2
        third_obj = "three"
        fourth_obj = False
        # put four objects into our linked list
        self.ll.append(first_obj)
        self.ll.append(second_obj)
        self.ll.append(third_obj)
        self.ll.append(fourth_obj)
        # reverse our linked list
        self.ll.reverse()

        new_obj = "new object!"
        # append a new object to the linked list
        self.ll.append(new_obj)
        # and create an expected string representation
        expected_str = "False -> three -> 2 -> one -> new object!"

        # we can test by get
        actual_obj = self.ll.get(4)
        # we can test by the string representation too
        actual_str = self.ll.__str__()

        # compare the two objects
        self.assertEqual(actual_obj, new_obj)
        self.assertEqual(actual_str, expected_str)

    def test_prepend_after_reverse(self):
        first_obj = "one"
        second_obj = 2
        third_obj = "three"
        fourth_obj = False
        # put four objects into our linked list
        self.ll.append(first_obj)
        self.ll.append(second_obj)
        self.ll.append(third_obj)
        self.ll.append(fourth_obj)
        # reverse our linked list
        self.ll.reverse()

        new_obj = "new object!"
        # prepend a new object to the linked list
        self.ll.prepend(new_obj)
        # and create an expected string representation
        expected_str = "new object! -> False -> three -> 2 -> one"

        # we can test by get
        actual_obj = self.ll.get(0)
        # we can test by the string representation too
        actual_str = self.ll.__str__()

        # compare the two objects
        self.assertEqual(actual_obj, new_obj)
        self.assertEqual(actual_str, expected_str)

if __name__ == '__main__':
    unittest.main(exit=False)
