from stack import *
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        # create a generic stack
        self.generic_stk = Stack()
        # and create a few objects
        first_obj = "Object!"
        second_obj = 2
        third_obj = False

    def test_stack_initialization(self):
        # create a basic stack
        stack_init = Stack()
        # then test it's class
        self.assertTrue(isinstance(stack_init, Stack))

    def test_stack_empty(self):
        # check if the generic stack is empty
        assertTrue(self.generic_stk.is_empty())

    def test_stack_empty_via_string(self):
        # make an expected output
        expected = "Stack is empty!"
        # get the actual output
        actual = self.generic_stk.__str__()
        # check if the expected is equal to the actual
        assertEqual(actual, expected)

    def test_stack_empty_via_pop(self):
        # the generic stack is empty on intialization, so just pop it
        self.assertRaises(StackEmptyException, self.generic_stk.pop)

    def test_push_once_is_empty(self):
        # add an object to the stack
        self.generic_stk.push(first_obj)
        # then test whether or not it is empty
        self.assertFalse(self.generic_stk.is_empty())

    def test_push_once_via_string(self):
        # add an object to the stack
        self.generic_stk.push(first_obj)
        # make an expected string
        expected = "Object!\n---"
        # then get the actual string
        actual = self.generic_stk.__str__()
        # then test the equivalence of the two
        self.assertEqual(actual, expected)

    def test_push_once_via_pop(self):
        # set an expected object
        expected = first_obj
        # add the object to the stack
        self.generic_stk.push(expected)
        # then pop the object out of the stack
        actual = self.generic_stk.pop()
        # check the equivalence of the two
        self.assertEqual(actual, expected)

    def test_push_twice_is_empty(self):
        # add two objects to the stack
        self.generic_stk.push(first_obj)
        self.generic_stk.push(second_obj)
        # then test whether the stack is empty
        self.assertFalse(self.generic_stk.is_empty())

    def test_push_twice_via_string(self):
        # add two objects to the stack
        self.generic_stk.push(first_obj)
        self.generic_stk.push(second_obj)
        # create a string where the most recent object is on the top
        expected = "2\n---\nObject!\n---"
        # then get the actual string representation
        actual = self.generic_stk.__str__()
        # test the equivalence of the two
        self.assertEqual(actual, expected)

    def test_push_twice_via_pop_once(self):
        # add two objects to the stack
        self.generic_stk.push(first_obj)
        self.generic_stk.push(second_obj)
        # the second object is the expected
        expected = second_obj
        # then pop one object from the stack
        actual = self.generic_stk.pop()
        # check if they are the same object
        assertEqual(actual, expected)
        # then check if the stack is not empty
        self.assertFalse(self.generic_stk.is_empty())

    def test_push_twice_via_pop_twice(self):
        # add two objects to the stack
        self.generic_stk.push(first_obj)
        self.generic_stk.push(second_obj)
        # the second object is the first object expected to be popped
        expected_first = second_obj
        # followed by the first object...
        expected_second = first_obj

        # get both objects from the stack
        actual_first = self.generic_stk.pop()
        actual_second = self.generic_stk.pop()
        # check the equivalence of the two
        self.assertEqual(actual_first, expected_first)
        self.assertEqual(actual_second, expected_second)

        # then check if the stack is empty
        self.assertTrue(self.generic_stk.is_empty())

    def test_push_three_via_string(self):
        # add three objects to the stack
        self.generic_stk.push(first_obj)
        self.generic_stk.push(second_obj)
        self.generic_stk.push(third_obj)
        # create an expected string representation of the stack
        expected = "False\n---\n2\n---\nObject!\n---"
        # get the actual representation
        actual = self.generic_stk.__str__()
        # check the equivalence of the two objects
        self.assertEqual(actual, expected)

    def test_push_three_via_pop_once(self):
        # add three objects to the stack
        self.generic_stk.push(first_obj)
        self.generic_stk.push(second_obj)
        self.generic_stk.push(third_obj)
        # the expected object is the third object
        expected = third_obj
        # the actual object is what is at the top of the stack
        actual = self.generic_stk.pop()
        # check the equivalence of the two
        self.assertEqual(actual, expected)
        # and then check if the stack is empty
        self.assertFalse(self.generic_stk.is_empty())

    def test_push_three_via_pop_three(self):
        # add three objects to the stack
        self.generic_stk.push(first_obj)
        self.generic_stk.push(second_obj)
        self.generic_stk.push(third_obj)
        # then make a list of expected objects in sequential order
        expected_list = [third_obj, second_obj, first_obj]
        # go through a while loop
        while (not self.generic_stk.is_empty()):
            # get an expected value
            expected = expected_list[0]
            # and then the actual value
            actual = self.generic_stk.pop()
            # test the two
            self.assertEqual(actual, expected)
            # then delete the first element in the expected list
            del expected_list[0]

if __name__ == '__main__':
    unittest.main(exit=False)
