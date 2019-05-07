# peak finding


def one_dim_peak_find_faster(given_list):
  '''
  (list of ints) -> int

  Given a list, return the peak of the list

  A peak is defined such that L[i] >= L[i+1] and L[i] >= L[i-1]

  if i == 0 and the length of L is greater than 1,
  then L has a peak when L[i] >= L[i+1]

  if i == len(L) - 1 and the length of L is greater than 1, then L has a peak
  when L[i] >= L[i-1]

  if len(L) == 1, then the list is a peak
  '''
  # one thing that we want is the length of the list, divided by 2
  mid_index = int(len(given_list) / 2)  # this is naturally floored
  # Base case: if the list is empty, return None
  if (given_list == []):
    return None
  # Base case: if the given list has one element, then it is a peak
  elif (len(given_list) == 1):
    return given_list[0]
  # Base case: only two elements; "RS" will index mid + 1 and mid - 1
  # which may have an indexing error (i.e. L[2] does not exist)
  elif (len(given_list) == 2):
    #  return the higher index
    if given_list[0] >= given_list[1]:
      return 0
    else:
      return 1
  # Otherwise
  else:
    # compare the midpoint with the element before and the element after
    if (given_list[mid_index - 1] >= given_list[mid_index]):
      # it would be fair to call this recursively because we don't
      # necessarily have to include the midpoint anymore
      return one_dim_peak_find_faster(given_list[:mid_index])
    elif (given_list[mid_index + 1] >= given_list[mid_index]):
      # if this were to be the case, we return the mid point index
      # and find a peak with a new list
      val = mid_index + 1
      val += one_dim_peak_find_faster(given_list[mid_index + 1:])
      return val
    else:
      # the midpoint is a peak
      return mid_index

if __name__ == "__main__":
  L0 = [] # return None
  L1 = [1] # return 0
  L2 = [1, 1] # return 0
  L3 = [2, 1] # return 0
  L4 = [1, 2] # return 1
  L5 = [1, 1, 1] # return 1
  L6 = [1, 2, 3] # return 2
  L7 = [3, 2, 1] # return 0
  L8 = [1, 2, 9, 6, 5, 6, 7, 8, 9] # return 2
  L9 = [6, 7, 8, 2, 5, 9, 10, 3, 1] # return 6
  L10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # return 12
  L11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 12, 13] # return 10
  print(one_dim_peak_find_faster(L9))
  print(one_dim_peak_find_faster(L10))
  print(one_dim_peak_find_faster(L11))
