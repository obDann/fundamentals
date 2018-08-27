from queue import *
import unittest


class TestQueue(unittest.TestCase):

    def setUp(self):
        # create a basic queue
        self.generic_q = Queue()

    def test_queue_initialization(self):
        # initialize the queue
        queue_init = Queue()
        # test if the queue is a queue as it may be None object
        self.assertTrue(isinstance(queue_init, Queue))

    def test_queue_empty_str(self):
        # make an expected string
        expected = "Queue is empty!"
        # with our queue that we set up, test it's typecast to string
        actual = str(self.generic_q)
        self.assertEqual(actual, expected)

    def test_enqueue_once(self):
        # we're just going to aggregate the typecase to string
        # so we make an expected string
        expected = "4\n---"
        # then we want to enqueue a 4 to the Queue
        self.generic_q.enqueue(4)
        # we make the actual string
        actual = str(self.generic_q)
        # then test the two
        self.assertEqual(actual, expected)

    def test_enqueue_twice(self):
        # again, we're going to aggregate the typecast to string
        # so we make an expected string
        expected = "4\n---\nThis is a string\n---"
        # and then we want to enqueue two items
        self.generic_q.enqueue(4)
        self.generic_q.enqueue("This is a string")
        # make the actual string
        actual = str(self.generic_q)
        # then test the two
        self.assertEqual(actual, expected)

    def test_empty(self):
        # we assume that the queue is empty
        self.assertTrue(self.generic_q.is_empty())

    def test_not_empty(self):
        # enqueue an item to our generic queue
        self.generic_q.enqueue("object")
        # then test if it is empty
        self.assertFalse(self.generic_q.is_empty())

    def test_dequeue_empty(self):
        # assume that our initialized queue is empty
        self.assertRaises(QueueEmptyException, self.generic_q.dequeue)

    def test_dequeue_once(self):
        expected = "This is a string!"
        # aggregate the enqueue method with our expected val
        self.generic_q.enqueue(expected)
        # then we want to dequeue it
        actual = self.generic_q.dequeue()
        # then we test if the actual value is the same
        # as the expected value
        self.assertEqual(actual, expected)

    def test_dequeue_twice(self):
        expected_first = "This is a string!"
        expected_second = 4
        # aggregate the enqueue method with
        # our expected values
        self.generic_q.enqueue(expected_first)
        self.generic_q.enqueue(expected_second)
        # then we want to dequeue our values
        actual_first = self.generic_q.dequeue()
        actual_second = self.generic_q.dequeue()
        # then we test if the actual values are the same
        # as the expected values
        self.assertEqual(actual_first, expected_first)
        self.assertEqual(actual_second, expected_second)

if __name__ == '__main__':
    unittest.main(exit=False)
