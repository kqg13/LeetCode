# 2661: First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/
# https://leetcode.com/problems/first-completely-painted-row-or-column/discuss/3470232/Python3-Solution

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        # Pre-process the matrix
        pre_process_d = dict()
        m, n = len(mat), len(mat[0])

        # O(m x n)
        for i in range(m):
            for j in range(n):
                ele = mat[i][j]
                pre_process_d[ele] = (i, j)

        # Initialize two frequency lists
        row_freq, col_freq = [0] * m, [0] * n

        # O(m x n)
        # Go through arr and increment frequencies
        for i, num in enumerate(arr):
            r_idx, c_idx = pre_process_d[num]
            row_freq[r_idx] += 1
            col_freq[c_idx] += 1
            if row_freq[r_idx] == n or col_freq[c_idx] == m:
                return i


s = Solution()
arr1, mat1 = [1, 3, 4, 2], [[1, 4], [2, 3]]
arr2, mat2 = [2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
