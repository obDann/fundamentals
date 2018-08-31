def selection_sort(L):
    '''
    (List of comparable objs) -> List of comparable objs

    O(n^2) sorting algorithm

    Returns a list of sorted objects from the passed list
    '''
    # copy the passed list so that we can return the sorted list
    ret = L[:]

    # then go through the list
    for i in range(len(ret)):
        # we want the smallest valued object to be at index i
        smallest_index = i
        smallest = ret[smallest_index]
        # then we want to look at the rest of the list
        for j in range(i, len(ret)):
            # check if there exists a smaller value than our "determined"
            # smallest value
            if ret[j] < smallest:
                # if there is a smaller value, then we want to state that
                # there is a smaller value
                smallest = ret[j]
                smallest_index = j
        # once we have found the index of the smallest value, we want the
        # left side of the list (ret[:i]) to be sorted
        # so we swap the values
        swap(ret, i, smallest_index)

    # then return the list
    return ret


def swap(L, i, j):
    '''
    (List of objs, int, int) -> None

    Swaps two indexed values from the list
    '''
    L[i], L[j] = L[j], L[i]
