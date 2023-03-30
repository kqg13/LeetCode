# Hard DP: Max Sum Increasing Subsequence

# Given a non-empty array of integers, write a function that returns an array of length 2. The first element in the
# output array should be an int representing the greatest sum that can be generated from a strictly-increasing sub-
# sequence in the array. The second element should be an array of the numbers in that subsequence. A subsequence is
# defined as a set of nums that are not necessarily adjacent but that are in the same order as they appear in the
# array. Assume there will only be one increasing subsequence with the greatest sum.

# Sample input: [4, 6, 1, 3, 8, 4, 6]
# Sample output: [18, [4, 6, 8]]


# Time: O(N^2), Space: O(N)
def maxSumIncreasingSubsequence(array):
    sums = array[:]
    sequences = [i for i in range(len(array))]
    # sequences = [None] * (len(array))
    max_idx = 0

    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i] and sums[j] + array[i] >= sums[i]:
                sums[i] = sums[j] + array[i]
                sequences[i] = j

        if sums[i] >= sums[max_idx]:
            max_idx = i
    # max_idx = sums.index(max(sums))

    return [sums[max_idx], getSequence(array, sequences, max_idx)]


def getSequence(array, sequences, i):
    nums = [array[i]]
    # Trace steps
    while i != 0:
        nums.append(array[sequences[i]])
        i = sequences[i]
    return list(reversed(nums))


# lst = [4, 6, 1, 3, 8, 4, 6]  # Max = 18
lst = [10, 70, 20, 30, 50, 11, 30]
print(maxSumIncreasingSubsequence(lst))
