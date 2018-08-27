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

    def __str__(self):
        '''
        (Node) -> str

        Returns a string representation of the nodes
        '''
        # just use a helper function...
        return self._str_helper()

    def _str_helper(self):
        '''
        (Node) -> str

        Returns the string representation of the current node
        '''
        # create a returing string
        ret = ""
        # base case: there isn't a next node
        if (not self.next):
            # then we just return the string representation of this node
            ret = str(self.data)
        # RD: there is a next node
        else:
            # in this case, we get the current node's data string
            # representation and add an arrow to it
            ret = str(self.data) + " -> "
            # then add the next node's string representation
            ret += self.next._str_helper()
        # then return our string representation
        return ret


class LinkedList():

    def __init__(self):
        '''
        (LinkedList) -> None

        Initializes a linked list
        '''
        # REPRESENTATION INVARIANT
        #
        # _num_ele is the number of nodes there are in the linked
        # list
        #
        # _head is either None or a node
        # _tail is either None or a node
        # if _head is None:
        #     the linked list is empty
        #     _tail is None
        # otherwise:
        #     _head is the first node of the linked list
        #     _tail is the last node of the linked list
        #     if node A is placed before node B:
        #         A.next_node[.next_node]* = B

        # on initialization, set the number of elements in the list as 0
        self._num_ele = 0
        # on initialization, the head and the tail are None
        self._head = None
        self._tail = None

    def __str__(self):
        '''
        (LinkedList) -> str

        Returns a string representation similar to the following:
        x -> x -> x -> x...

        where x are objects within the linked list
        '''
        # create a returning string
        ret = ""
        # check if the linked list is empty
        if (self.is_empty()):
            ret = "Linked list is empty!"
        # otherwise, we can use the node's string representation
        else:
            ret = str(self._head)
        # then return the string
        return ret

    def append(self, obj):
        '''
        (LinkedList, obj) -> None

        Adds the object to the end of the linked list
        '''
        # first, create a node for the object
        new_node = Node(obj)

        # check if the head is None
        if (not self._head):
            # if it is, then we can set our head to the new node
            self._head = new_node

        # we can check if the tail is not None
        if (self._tail):
            # if it isn't then we can append to our linked list
            self._tail.next = new_node

        # in both possible scenarios, the tail is the new node
        self._tail = new_node

        # and we increment the number of elements there are in the linked list
        self._num_ele += 1

    def prepend(self, obj):
        '''
        (LinkedList, obj) -> None

        Adds the object to the beginning of the linked list
        '''
        # we can create an node for the object and point it to the head
        # of the linked list
        new_node = Node(obj, self._head)
        # then we can set the head to be the new node
        # we don't care if self._head is originally None or a Node
        self._head = new_node
        # and we can increment the number of elements there are in the
        # linked list
        self._num_ele += 1
        # and we have to check if there is only one element
        if (self._num_ele == 1):
            # if there is only one element, then we have to specify the
            # tail is that node as well
            self._tail = new_node

    def get_num_elements(self):
        '''
        (LinkedList) -> int

        Returns the number of elements there are in the linked list
        '''
        # just return the number of elements there are in the linked list
        return self._num_ele

    def insert(self, obj, index):
        '''
        (LinkedList, obj, int) -> None

        Inserts the object at a specified index

        RAISES BoundaryException when the index is not in the following range:
        0 <= index <= number_of_elements
        '''
        # check if the passed index is out of bounds from our specified range
        too_low = index < 0
        too_high = index > self._num_ele
        if (too_low or too_high):
            # create a message
            msg = "The index must be in the range of 0 <= index <= "
            msg += str(self._num_ele)
            # then raise the exception
            raise BoundaryException(msg)

        # we consider two instantaneous cases:
        # first, the index is 0
        if (index == 0):
            # if it is, then we just prepend it
            self.prepend(obj)
        # second, is if the index is the number of elements in the list
        elif (index == self._num_ele):
            # if it is, then we append it
            self.append(obj)
        else:
            # otherwise, the index is at an arbitrary position
            # so, the node that we do want is the node before the specified
            # index. Special thanks to our (static) helper function.
            before = LinkedList._traverse_to_node_by_index(self._head,
                                                           index - 1)
            # then we want to create a node of the object given to us
            to_insert = Node(obj)
            # we want the new node to point to before's next node
            to_insert.next = before.next
            # then we want the node before to point to the new node
            before.next = to_insert
            # and we can now increment the number of elements there are in
            # the linked list
            self._num_ele += 1

    def get(self, index):
        '''
        (LinkedList, int) -> obj

        Returns the object at the specified index

        RAISES BoundaryException when the index is not in the following range:
        0 <= index < number_of_elements
        OR if the linked list is empty
        '''
        # first, we check if the index is too high or too low
        too_low = index < 0
        too_high = index >= self._num_ele
        if (too_low or too_high):
            # create a message
            msg = "The index must be in the range of 0 <= index < "
            msg += str(self._num_ele)
            # then raise the exception
            raise BoundaryException(msg)

        # create a returning value
        ret = None
        # then we can check our instantaneous cases
        # first case: is if the specified index is the head
        if (index == 0):
            ret = self._head.data
        # second case: is if the specified index is the tail
        elif (index == self._num_ele - 1):
            ret = self._tail.data
        # otherwise, we are at an arbitrary node
        else:
            # in this case, we specify the node we want
            arbitrary_node = LinkedList._traverse_to_node_by_index(self._head,
                                                                   index)
            # and then we return the contents of that node
            ret = arbitrary_node.data
        # then return the specified data
        return ret

    def remove(self, index):
        '''
        (LinkedList, int) -> None

        Removes an object from the linked list

        RAISES BoundaryException when the index is not in the following range:
        0 <= index < number_of_elements
        OR if the linked list is empty
        '''
        # first, we check if the index is too high or too low
        too_low = index < 0
        too_high = index >= self._num_ele
        if (too_low or too_high):
            # create a message
            msg = "The index must be in the range of 0 <= index < "
            msg += str(self._num_ele)
            # then raise the exception
            raise BoundaryException(msg)

        # then we can really only consider one instantaneous case, where the
        # specified index is the head
        if (index == 0):
            # if this is the case, then set our head to be the next node
            self._head = self._head.next
            # and we want to check if the head is None
            if (not self._head):
                # if it is, according to our representation invariant,
                # the tail is supposed to be None as well
                self._tail = None
        # otherwise, the node specified is at an arbitrary node
        else:
            # we get the node before the indicated index (thanks to our
            # static method)
            before = LinkedList._traverse_to_node_by_index(self._head,
                                                           index - 1)
            # in this case, if the index is the same as the tail, the
            # tail changed to before
            if (index == self._num_ele - 1):
                tail = before
            # we can get the node that is right after the indicated index
            after = before.next.next
            # then we can remove the specified node
            before.next = after

        # in all cases, we have lost an element so we decrement the number
        # of elements in the linked list
        self._num_ele -= 1

    def is_empty(self):
        '''
        (LinkedList) -> boolean

        Determines if the linked list is empty
        '''
        # as per our representation invariant, return the following
        # condition
        return self._head is None

    def reverse(self):
        '''
        (LinkedList) -> None

        Reverses the ordering of the linked list
        '''
        # in this case, we can just call our helping static method
        LinkedList._reverse_list(self._head)
        # in all possible cases, we want to switch the tail and the head
        # so we hold the head
        hold = self._head
        # set the head to the tail
        self._head = self._tail
        # then set the tail to the head
        self._tail = hold

    @staticmethod
    def _traverse_to_node_by_index(curr_node, curr_index):
        '''
        (Node, index) -> Node

        Traverses to a node at a specified index.

        This method is only used when an index is in range of:
        0 <= index < number_of_elements
        '''
        # interstingly enough, not putting "self" in a class is equivalent to
        # using a static method
        ret = None
        # base case: the current index is 0
        if (curr_index == 0):
            # if it is, then return the current node
            ret = curr_node
        # RD: the current index is still a positive integer
        else:
            # if it isn't, decrement the index
            curr_index -= 1
            # then traverse to the next node
            curr_node = curr_node.next
            # then the node to return is the recursive call
            ret = LinkedList._traverse_to_node_by_index(curr_node, curr_index)
        # then return our node
        return ret

    @staticmethod
    def _reverse_list(curr_node):
        '''
        (Node) -> Node

        Reverses and returns the connection of nodes
        '''
        # create a returning value
        ret = None
        # base case: the passed node is None or there is only one node
        if (not curr_node or not curr_node.next):
            # just return the current node
            ret = curr_node
        # RD: there is more than one node
        else:
            # reverse the rest of the linked list
            rever = LinkedList._reverse_list(curr_node.next)
            # once we reversed the rest of the linked list
            # set the reversed node's next pointer to be the current node
            rever.next = curr_node
            # then set the current node's next to none as it's still pointing
            # to rever
            curr_node.next = None
            # then return the current node
            ret = curr_node
        return ret
