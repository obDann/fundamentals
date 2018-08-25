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


    def __str__(self):
        '''
        (Queue) -> str

        Returns a string representation of the queue
        '''

    def enqueue(self, obj):
        '''
        (Queue, obj) -> None

        Adds an object to the queue. This method mutates the Queue.
        '''

    def dequeue(self):
        '''
        (Queue) -> obj

        Removes and returns the earliest object that entered the queue. This
        method mutates the Queue
        '''


    def is_empty(self):
        '''
        (Queue) -> boolean

        Returns true iff the queue is empty
        '''
