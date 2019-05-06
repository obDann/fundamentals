# 1D peak finding

# When given a list,
# Look at the x = floor(n / 2) element

# if L[x] < L[x - 1] then
#   Look at the left half of the peak

# elif L[x] < L[x + 1] then
#   Look at the right half of the peak

# else:
#    Position at L[x] is a peak