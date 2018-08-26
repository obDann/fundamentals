class QueueEmptyException(Exception):
    '''
    An exception when a queue is empty
    '''


class Queue():

    def __init__(self):
        '''
        (Queue) -> None

        Initializes a container that is first-in first-out
        '''
        # REPRESENTATION INVARIANT
        # q is a list of objects
        #
        # if an object o is enqueued then:
        #     q[0] will hold object o, incrementing
        #     the indexes of existing objects in the
        #     queue by 1
        #
        # if the queue is dequeued then:
        #     q[0] will be removed from the list, decrementing the
        #     indexes of the existing objects in the queue by 1
        #
        # The queue is empty iff q == []

        # initialize the queue
        self._q = []

    def __str__(self):
        '''
        (Queue) -> str

        Returns a string representation of the queue
        '''
        # create a returning value
        ret = ""
        # first check if the queue is empty
        if (self.is_empty()):
            # if it is, then our returning value is the following string
            ret = "Queue is empty!"
        else:
            # we make a current index to be the last element
            curr_index = len(self._q) - 1
            # then we want to set our returning string to our helper
            # function
            ret = self._str_helper(curr_index)
        return ret

    def _str_helper(self, curr_index):
        '''
        (Queue, int) -> str

        A helper function to provide a string representation
        '''
        # create a returning string
        ret = ""
        # base case: there is only one element
        if (curr_index == 0):
            # then we just return the string representation of the first
            # element
            ret = self._q[curr_index].__str__() + "\n---"
        # RD: an arbitrary element
        else:
            # get the current element's string representation
            curr = self._q[curr_index].__str__() + "\n---"
            # decrement the index
            curr_index -= 1
            # then we want to get the previous elements to put below
            # current element's string representation
            below = self._str_helper(curr_index)
            # then bind the stack of elements with a new line
            ret = curr + "\n" + below
        return ret

    def enqueue(self, obj):
        '''
        (Queue, obj) -> None

        Adds an object to the queue. This method mutates the Queue.
        '''
        # just prepend the object
        self._q.insert(0, obj)

    def dequeue(self):
        '''
        (Queue) -> obj

        Removes and returns the earliest object that entered the queue. This
        method mutates the Queue

        RAISES QueueEmptyException if the queue is empty
        '''
        # check if the object is empty
        if (self.is_empty()):
            # if it is, then we want to raise an error
            raise QueueEmptyException("Cannot dequeue as the Queue is empty")
        # otherwise we can just pop the first object
        return self._q.pop()

    def is_empty(self):
        '''
        (Queue) -> boolean

        Returns true iff the queue is empty
        '''
        # as per our representation invariant, the queue is empty iff
        return self._q == []
