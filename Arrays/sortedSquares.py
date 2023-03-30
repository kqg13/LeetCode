# Easy array problem 977: Squares of a Sorted Array

# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.

# Example: Input: [-4, -1, 0, 3, 10], Output: [0, 1, 9, 16, 100]


class Solution:
    def sortedSquares(self, A):
        """
        :param A: List[int]
        :return: List[int]
        """
        return sorted(x * x for x in A)
