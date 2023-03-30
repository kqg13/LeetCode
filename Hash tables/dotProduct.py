# 1570: Dot Product of Two Sparse Vectors
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/


class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        dot_product = 0
        for k, v in self.d.items():
            if k in vec.d:
                dot_product += v * vec.d[k]
        return dot_product


nums1, nums2 = [1, 0, 0, 2, 3], [0, 3, 0, 4, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
