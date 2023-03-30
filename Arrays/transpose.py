# Easy problem 867: Transpose Matrix

# Given a matrix A, return the transpose of A. The transpose of a matrix is the
# matrix flipped over it's main diagonal, switching the row and column indices
# of the matrix.


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        ans = [[None] * rows for _ in range(cols)]  # "insight": need to setup transpose otherwise out of range on A
        for r, row in enumerate(A):  # 0, 1
            for c, val in enumerate(row):  # 0, 1, 2
                ans[c][r] = val

        return ans
