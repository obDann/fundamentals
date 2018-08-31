from min_heap import *

def heap_sort(L):
    '''
    ([List of comparable objs]) -> [List of comparable objs]

    O(nlog(n)) sorting algorithm

    Returns a list of sorted objects from the passed list
    '''
    # create a heap
    pipe = MinHeap()
    # and create a returning list
    ret = []
    # iterate through the list
    for obj in L:
        # add the object to the heap
        pipe.insert(obj)

    # go through the heap
    while (not pipe.is_empty()):
        # and have the returning list append the popped object
        popped = pipe.remove_min()
        # and add it to the returning list
        ret.append(popped)

    # then return the returning list
    return ret
