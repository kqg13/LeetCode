# Easy problem 832: Flipping an image


# Given a binary matrix A, we want to flip the image horizontally, then invert
# it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is
# replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return []

        inverted = []
        for matrix in A:
            inverted.append([1 if bit == 0 else 0 for bit in matrix[::-1]])
        return inverted

    def flipAndInvertImageCleaner(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[bit ^ 1 for bit in row[::-1]] for row in A]  # ^ is xor
