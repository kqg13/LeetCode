# Hard DP problem: Minimum Number of Jumps

# You are given a non-empty array of ints.  Each element represents the max
# number of steps you can take forward. For example, if the element at index 1
# is 3, you can go from index 1 to index 2, 3, or 4. Write a function that
# returns the minimum number of jumps needed to reach the final index. Note
# that jumping from index i to index i + x always constitutes 1 jump, no matter
# how large x is.


# Time: O(N^2), Space: O(N)
def minNumberOfJumps(array):
    jumps = [float('inf')] * len(array)
    jumps[0] = 0

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]

# Time: O(N), Space: O(N)
def minNumberOfJumpsBetter(array):
    return 0


arr = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(minNumberOfJumps(arr))
print(minNumberOfJumpsBetter(arr))
