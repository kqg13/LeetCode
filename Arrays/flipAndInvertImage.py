# Easy problem 832: Flipping an image


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


s = Solution()
A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
print(s.flipAndInvertImage(A))
print(s.flipAndInvertImageCleaner(A))
