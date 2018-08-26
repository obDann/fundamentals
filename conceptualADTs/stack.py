class StackEmptyException(Exception):
    '''
    An exception when a stack is empty
    '''


class Stack():

    def __init__(self):
        '''
        (Stack) -> None

        Initializes the stack
        '''
        # REPRESENTATION INVARIANT
        # stk is a list
        #
        # stk is empty when:
        #     stk == []
        #
        # if an object o has been pushed onto the stack:
        #     stk appends object o (as the last element of the list)
        #
        # if an object o is popped from the stack
        #     stk removes and returns object o from the list

        # just initialize a list
        self._stk = []

    def __str__(self):
        '''
        (Stack) -> str

        Returns a string representation of the stack
        '''
        # create a returning string
        ret = ""
        # check if the stack is empty
        if (self.is_empty()):
            # if it is, then we want our string to say the following
            ret = "Stack is empty!"
        # otherwise, we can assume that the stack has at least one element
        else:
            # so we call our helper function
            ret = self._str_helper()
        # then return the output
        return ret

    def _str_helper(self, curr_index=0):
        '''
        (Stack, int) -> str

        A helper function for the string representation of the stack
        '''
        # create a returning string
        ret = ""
        # base case: the current index is the last element
        if (curr_index == len(self._stk) - 1):
            # if it is, then we return the string representation of that
            # only element
            ret = self._stk[curr_index].__str__() + "\n---"
        # RD: otherwise, we can assume that there is more than one element
        else:
            # get the string representation of the current element indicated
            # by the current index
            curr_ele = self._stk[curr_index].__str__() + "\n---"
            # increment the current index
            curr_index += 1
            # then we want to get the rest of the stack
            rest = self._str_helper(curr_index)
            # given our representation invariant, it is sensible to put
            # the current element below the stack
            ret = rest + "\n" + curr_ele
        # then return our string
        return ret

    def push(self, obj):
        '''
        (Stack, obj) -> None

        Adds the object to the top of the stack. This method mutates the stack.
        '''
        # just append the object to our list
        self._stk.append(obj)

    def pop(self):
        '''
        (Stack) -> obj

        Removes and returns the object at the top of the stack

        RAISES StackEmptyException when the stack is empty
        '''
        # check if the stack is empty
        if (self.is_empty()):
            # if it is, then we want to raise an error
            raise StackEmptyException("There are no elements in the stack"
                                      + " to pop")
        # otherwise, we can assume that there are elements in the stack
        # so we can just pop it
        return self._stk.pop()

    def is_empty(self):
        '''
        (Stack) -> boolean

        Determines if the stack is empty
        '''
        # just return our condition as stated from our representation
        # invariant
        return self._stk == []
