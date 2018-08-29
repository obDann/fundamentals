class HeapEmptyException(Exception):
    '''
    An exception that occurs when there is an attempt to remove an element
    from an empty heap
    '''

class MinHeap():

    def __init__(self):
        '''
        (MinHeap) -> None

        Initializes the heap
        '''

    def insert(self, new_val):
        '''
        (MinHeap, float) -> None

        Inserts an object to the MinHeap
        '''

    def remove_min(self):
        '''
        (MinHeap) -> float

        Removes the smallest value in the heap

        RAISES HeapEmptyException when the heap is empty
        '''

    def is_empty(self):
        '''
        (Minheap) -> boolean

        Determines whether the heap is empty or not
        '''
