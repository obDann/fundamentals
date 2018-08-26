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

    def __str__(self):
        '''
        (Stack) -> str

        Returns a string representation of the stack
        '''

    def push(self, obj):
        '''
        (Stack, obj) -> None

        Adds the object to the top of the stack. This method mutates the stack.

        RAISES StackEmptyException when the stack is empty
        '''

    def pop(self):
        '''
        (Stack) -> obj

        Removes and returns the object at the top of the stack
        '''

    def is_empty(self):
        '''
        (Stack) -> boolean

        Determines if the stack is empty
        '''
