class BoundaryException(Exception):
    '''
    An exception that occurs when a passed index is out of bounds
    '''


class Node():

    def __init__(self, data, next=None):
        '''
        (Node, obj, Node) -> None

        Initializes a unary node
        '''
        # REPRESENTATION INVARIANT
        # data holds the content in the node
        # next is a pointer to a node

        # just initialize our data and next
        # in this case, it is sensible to make things public
        self.data = data
        self.next = next


class LinkedList():

    def __init__(self):
        '''
        (LinkedList) -> None

        Initializes a linked list
        '''
        # REPRESENTATION INVARIANT
        #
        # self._num_ele is the number of nodes there are in the linked
        # list
        #
        # self._head is either None or a node
        # self._tail is either None or a node
        # if self._head is None:
        #     the linked list is empty
        #     self._tail is None
        # otherwise:
        #     self._head is the first node of the linked list
        #     self._tail is the last node of the linked list
        #     if node A is placed before node B:
        #         A.next_node[.next_node]* = B

    def __str__(self):
        '''
        (LinkedList) -> str

        Returns a string representation similar to the following:
        x -> x -> x -> x...

        where x are objects within the linked list
        '''

    def append(self, obj):
        '''
        (LinkedList, obj) -> None

        Adds the object to the end of the linked list
        '''

    def prepend(self, obj):
        '''
        (LinkedList, obj) -> None

        Adds the object to the beginning of the linked list
        '''

    def get_num_elements(self):
        '''
        (LinkedList) -> int

        Returns the number of elements there are in the linked list
        '''

    def insert(self, obj, index):
        '''
        (LinkedList, obj, int) -> None

        Inserts the object at a specified index

        RAISES BoundaryException when the index is not in the following range:
        0 <= index < number_of_elements
        '''

    def get(self, index):
        '''
        (LinkedList, int) -> obj

        Returns the object at the specified index

        RAISES BoundaryException when the index is not in the following range:
        0 <= index < number_of_elements
        '''

    def is_empty(self):
        '''
        (LinkedList) -> boolean

        Determines if the linked list is empty
        '''
