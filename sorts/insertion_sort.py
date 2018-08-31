def insertion_sort(L):
    '''
    (List of comparable objs) -> List of comparable objs

    O(n^2) sorting algorithm

    Returns a list of sorted objects from the passed list
    '''
    # copy the passed list so that we can return the sorted list
    ret = L[:]
    # and set the number of elements as a variable
    num_ele = len(ret)

    # then go through the list
    for i in range(num_ele):
        # we assume that the list L[:i] is sorted
        # so we get the current element
        curr_ele = ret[i]

        # we want to place the element in the list where
        # L[j - 1] < curr_ele <= L[j]
        # s.t. j < i

        # so we want to traverse backwards in our sorted list
        j = i - 1
        # and we want to have a satisfiable condition
        satisfied = False
        # so we iterate backwards
        while (j >= 0 and not satisfied):
            # there are two cases that do arise, and it is when j = 0 and
            # when j != 0
            if (j == 0):
                # if this is the case, then we check if there is a satisfying
                # condition where
                if (ret[0] > curr_ele):
                    # pop the current element
                    curr_ele = ret.pop(i)
                    # then re-order the list
                    ret = [curr_ele] + ret
            else:
                # otherwise, we can assume that there are at least two elements
                # so, the satisfiable condition is when
                satisfied = ret[j - 1] < curr_ele
                satisfied = satisfied and (curr_ele <= ret[j])
                if (satisfied):
                    # if this is the case, we want to split the list into three
                    # where we have a middle element to remove from the list
                    mid_ele = [ret.pop(i)]
                    # then elements from j and onward
                    right_end = ret[j:]
                    # and the elements before j
                    left_end = ret[:j]
                    # then we redefine the list
                    ret = left_end + mid_ele + right_end
            # decrement
            j -= 1
    # then we can return our list
    return ret
