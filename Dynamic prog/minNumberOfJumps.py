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


# Recursive
def jump(nums):
    return jump_helper(nums, 0)


def jump_helper(nums, start):
    if start >= len(nums) - 1:
        return 0
    min_jumps = float('inf')
    for i in range(start + 1, start + nums[start] + 1):
        min_jumps = min(min_jumps, 1 + jump_helper(nums, i))
    return min_jumps


arr1 = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
arr2 = [2, 3, 1, 1, 4]
arr3 = [2, 3, 0, 1, 4]
# print(jump(arr3))
print(minNumberOfJumps(arr3))
# print(minNumberOfJumpsBetter(arr1))
