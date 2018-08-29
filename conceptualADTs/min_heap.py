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
        # REPRESENTATION INVARIANT
        # _heap is a list
        # if _heap == []:
        #    the heap is empty
        # suppose i and j are integer values
        # if j = i * 2 + 1 or j = i * 2 + 2:
        #     _heap[i] is the parent of _heap[j]
        #     thus,
        #     _heap[i] <= _heap[j]
        self._heap = []

    def insert(self, new_val):
        '''
        (MinHeap, float) -> None

        Inserts an object to the MinHeap
        '''
        # we append the value to the heap
        self._heap.append(new_val)
        # then we get where the index is
        new_index = len(self._heap) - 1
        # then we bubble up
        self._bubble_up(new_index)

    def remove_min(self):
        '''
        (MinHeap) -> float

        Removes the smallest value in the heap

        RAISES HeapEmptyException when the heap is empty
        '''
        # first we check if the heap is empty
        if (self.is_empty()):
            # if it is, then raise an error
            msg = "There are no elements from the heap to remove from"
            raise HeapEmptyException(msg)

        # otherwise, we have a returning variable
        holder = self._heap[0]
        # we get the value from the bottom of the list to be put at the
        # top
        self._heap[0] = self._heap[-1]
        # then we pop off the last item
        self._heap.pop()
        # we bubble up at index 0
        self._bubble_down(0)
        # then we return our returning variable
        return holder

    def is_empty(self):
        '''
        (Minheap) -> boolean

        Determines whether the heap is empty or not
        '''
        # as per our representation invariant, the empty condition is
        return self._heap == []

    def _swap(self, i, j):
        '''
        (MinHeap, int, int) -> None

        Swaps two indexed values in the heap
        '''
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _bubble_up(self, c_index):
        '''
        (MinHeap, int) -> None

        After adding a value to the heap, this method maintains the
        heap property
        '''
        # get the parent index
        p_index = (c_index - 1) // 2
        # base case: parent index is a negative number
        # don't do anything
        # otherwise
        # check if the parent is bigger than the child
        if (self._heap[p_index] > self._heap[c_index] and p_index >= 0):
            # we want to swap the values
            self._swap(p_index, c_index)
            # then we want to recall bubble up with the parent's index
            # as we move up
            self._bubble_up(p_index)

    def _bubble_down(self, p_index):
        '''
        (MinHeap, int) -> None

        After removing a value, this method maintains the min heap property
        '''
        # get the left child and right child index
        lc_index = p_index * 2 + 1
        rc_index = p_index * 2 + 2
        # get the number of nodes there are
        num_nodes = len(self._heap)
        # we check if the parent is violating
        if self._violation(p_index):
            # if it does, then we assume that there is either 1 child or
            # two children
            # if there is only one child
            if (rc_index >= num_nodes):
                # then we swap the two
                self._swap(p_index, lc_index)
                # then we continually bubble down
                self._bubble_down(lc_index)
            else:
                # we get the child with the lower value
                if (self._heap[lc_index] < self._heap[rc_index]):
                    self._swap(p_index, lc_index)
                    self._bubble_down(lc_index)
                else:
                    self._swap(p_index, rc_index)
                    self._bubble_down(rc_index)

    def _violation(self, p_index):
        '''
        (Minheap, int) -> bool

        Given a parent index, this method determines if the child(ren)
        violates the MinHeap property
        '''
        # get the children's indexes
        lc_index = p_index * 2 + 1
        rc_index = p_index * 2 + 2
        # get the number of elements there are
        num_ele = len(self._heap)
        # we check if the left child doesn't exist
        if (lc_index >= num_ele):
            # if it doesn't exist, then it doesn't violate
            result = False
        elif(rc_index >= num_ele):
            # we assume that we have one child
            # we check if the left child violates, meaning that the
            # parent is bigger than the child
            result = self._heap[lc_index] < self._heap[p_index]
        else:
            # otherwise, if either child violates, then it's true
            result = self._heap[lc_index] < self._heap[p_index]
            result = result or self._heap[rc_index] < self._heap[p_index]
        return result
