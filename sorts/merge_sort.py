def merge_sort(L):
    '''
    (List of comparable objs) -> List of comparable objs

    O(nlog(n)) sorting algorithm

    Returns a list of sorted objects from the passed list
    '''
    # make a returning value
    ret = []

    # base case: the passed list is empty
    if (L == []):
        # if it is, then we return an empty list
        None
    # base case: the passed has one element
    elif (len(L) == 1):
        # if it is, we just return that one element of the list
        ret = [L[0]]
    # otherwise, we can assume that there is more than one element in the list
    else:
        # in this case, we get the "middle" index
        mid_index = len(L) // 2
        # we want to cut the list in half, so we declare a left half and
        # right half (the right half will have more elements if the
        # length of the list is odd, but this does not matter too much)
        left = L[:mid_index]
        right = L[mid_index:]
        # RD: assuming that our merge sort works, we sort our left and right
        # lists
        left = merge_sort(left)
        right = merge_sort(right)
        # then we go through the sorted left and right lists
        while (left != [] or right != []):
            # we check if there are elements in both left or right
            if (left != [] and right != []):
                # define a variable beforehand for an element to add
                ele_add = None
                # we compare the first elements of the left and right lists
                if (left[0] < right[0]):
                    # we want to get the smaller element first so we pop out
                    # the first element from the left index
                    ele_add = left.pop(0)
                else:
                    # continuing on, we get the smallest element of the list
                    ele_add = right.pop(0)
                # then add the element to our returning list
                ret.append(ele_add)
            # otherwise, we check if the left list is empty but the right
            # list is
            elif (left == [] and right != []):
                # if this is the case, we set our returning list to concatenate
                # the right list
                ret += right
                # then we set the right list to be an empty list (we're done)
                right = []
            # otherwise, we can assume that the right list is empty, but the
            # left list isn't
            else:
                # so we have our returning list add the left list
                ret += left
                # then we set the left list to be an empty list (we're done)
                left = []
    # then we return our list
    return ret
