# Hard: Subarray sort

# Write a function that takes in an array of integers of at least length 2. The function should return an array of the
# starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for
# the entire input array to be sorted. If the input array is already sorted, return [-1, 1]

# Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# Sample output: [3, 9]

# Approach:
# I.    Find the smallest number out of place
# II.   Find the largest number out of place
# III.  Find the correct positions in the array for I and II

# Time: O(N), Space: O(1)
def subarraySort(array):
    min_out_of_order, max_out_of_order = float('inf'), float('-inf')
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(array, i, num):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)

    if min_out_of_order == float('inf'):
        return [-1, -1]

    min_idx = 0
    while array[min_idx] < min_out_of_order:
        min_idx += 1

    max_idx = len(array) - 1
    while array[max_idx] > max_out_of_order:
        max_idx -= 1

    return [min_idx, max_idx]


def isOutOfOrder(array, i, num):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    else:
        return num > array[i + 1] or num < array[i - 1]
