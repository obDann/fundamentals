def quick_sort(L):
    '''
    (List of comparable objs) -> List of comparable objs

    O(n^2) sorting algorithm

    Returns a list of sorted objects from the passed list
    '''
    # create a returning list
    ret = []
    # base case: the list is empty; if it is, we don't need to do anything
    if (L != []):
        # in this case, we can access values in the list

        # in this implementation, we set the pivot to be the first element
        # in the list
        pivot = L[0]
        # and we make lists; one list that has objects greater than the pivot
        GT = []
        # and the other being less than or equal to the pivot
        LTE = []
        # we can go through the list, discounting the pivot
        for obj in L[1:]:
            # then check if the iterating object is greater than the pivot
            if (obj > pivot):
                # if it is, append the object to the greater than list
                GT.append(obj)
            # otherwise, append the object to the less than or equal to list
            else:
                LTE.append(obj)
        # RD: We can assume that quick sort can return the sorted lists of
        # our greater than list and our less than list

        # so we sort it, along with the pivot
        ret = quick_sort(LTE) + [pivot] + quick_sort(GT)
    # then we return the list
    return ret
