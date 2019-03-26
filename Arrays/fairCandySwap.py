# Easy array problem 888: Fair Candy Swap

# Alice & Bob have candy bars of different sizes: A[i] is size of the
# i-th bar of candy that Alice has, and B[j] is size of the j-th bar of
# candy that Bob has. Since they are friends, they would like to exchange
# 1 candy bar each so that after the exchange, they both have same total
# amount of candy.  The total amount of candy a person has is sum of the
# sizes of candy bars they have.
#
# Return an int array ans where ans[0] is the size of candy bar that
# Alice must exchange, and ans[1] is the size of candy bar that Bob
# must exchange. If there are multiple answers, you may return any.

# Example 1: Input: A = [1, 1], B = [2, 2] --> Output: [1, 2]
# Example 2: Input: A = [1, 2], B = [2, 3] --> Output: [1, 2]
# Example 3: Input: A = [2], B = [1, 3] --> Output: [2, 3]
# Example 4: Input: A = [1, 2, 5], B = [2,4] --> Output: [5, 4]


class Solution:
    def fairCandySwap(self, A, B):
        """
        :param A: List[int]
        :param B: List[int]
        :return: List[int]
        """
        sum_a, sum_b = sum(A), sum(B)
        set_b = set(B)  # O(1) lookup
        for x in A:
            b = ((sum_b - sum_a) // 2) + x
            if b in set_b:
                return [x, b]
