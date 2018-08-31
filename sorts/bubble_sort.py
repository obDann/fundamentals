def bubble_sort(L):
    '''
    (List of comparable objs) -> List of comparable objs

    O(n^2) sorting algorithm

    Returns a list of sorted objects from the passed list
    '''
    # create a returning list
    ret = L[:]
    # and we set a swap counter to an arbitrary non zero value
    swap_counter = -1
    # and we have an indexed value that determines where the right end of
    # the list is sorted
    sorted_at = len(ret)
    # so, this process will keep on continuing until there are no elements
    # left to swap
    while (swap_counter != 0):
        # in this case, we set our swap counter to 0
        swap_counter = 0
        # then we iterate through the list, from the beginning until the
        # list is sorted
        for i in range(sorted_at):
            # first, check if i + 1 is not equal to the sorted_at variable
            # so that we can bypass the out of bounds exception
            if (i + 1 != sorted_at):
                # we check if the value at L[i+1] is smaller than L[i]
                if (ret[i + 1] < ret[i]):
                    # if it is, we swap the two elements
                    ret[i], ret[i + 1] = ret[i + 1], ret[i]
                    # as a consequence, we increment our swap counter
                    swap_counter += 1
        # thus, we can conculde that L[sorted_at - 1:] is sorted after this
        # iteration, so we decrement sorted_at
        sorted_at -= 1
    # then we return our list
    return ret
