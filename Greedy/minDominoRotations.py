# Greedy problem 1007: Minimum Domino Rotations for Equal Row

# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
# We may rotate the ith domino, so that A[i] and B[i] swap values.

# Return the min # of rotations so that all the values in A are the same, or
# all the values in B are same. If it cannot be done, return -1.

# Examples:
# Input1: A = [2, 1, 2, 4, 2, 2], B = [5, 2, 6, 2, 3, 2] --> 2
# Explanation1: If we rotate the 2nd & 4th dominoes, we can make every value in the top row equal to 2
# Input2: A = [3, 5, 1, 2, 3], B = [3, 6, 3, 3, 4] --> -1
# Explanation2: not possible


# Time: O(N), Space: O(1)
class Solution:
    def minDominoRotations(self, A, B) -> int:
        topDom, bottomDom = A[0], B[0]
        self.constraint = 25000  # problem constraint: 2 <= A.length == B.length <= 2 * 10^4
        topDom_topMatch = self.minDominoHelper(A, B, topDom)
        bottomDom_topMatch = self.minDominoHelper(A, B, bottomDom)
        topDom_bottomMatch = self.minDominoHelper(B, A, topDom)
        bottomDom_bottomMatch = self.minDominoHelper(B, A, bottomDom)
        result = min(topDom_topMatch, bottomDom_topMatch, topDom_bottomMatch, bottomDom_bottomMatch)
        return -1 if result == self.constraint else result

    def minDominoHelper(self, A, B, match) -> int:
        rotations = 0
        for i in range(len(A)):
            if A[i] != match and B[i] != match:
                return self.constraint
            elif A[i] == match:
                continue
            elif B[i] == match:
                rotations += 1
        return rotations

    # Not used
    def getTop(self, A, B):
        topCount = 0
        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                continue
            elif B[i] == A[i + 1]:
                A[i], B[i] = B[i], A[i]
                topCount += 1
            elif A[i] == B[i + 1]:
                A[i + 1], B[i + 1] = B[i + 1], A[i + 1]
                topCount += 1
            elif B[i] == B[i + 1] and A[i] != A[i + 1]:
                A[i], B[i] = B[i], A[i]
                A[i + 1], B[i + 1] = B[i + 1], A[i + 1]
                topCount += 2
            if A[i] != A[i + 1] and A[i] != B[i + 1]:
                return -1
        return topCount


s = Solution()
