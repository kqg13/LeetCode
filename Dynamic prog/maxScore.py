# 1423: Maximum Points from Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints, k):
        """
        cardPoints: List[int]
        k: int
        return: int
        """
        self.cardPoints = cardPoints
        self.n = len(cardPoints) - 1
        front, back = 0, len(cardPoints) - 1
        result = self.maxScoreHelper(k, front, back)
        return result

    def maxScoreHelper(self, k, front, back):
        if k == 0 or front > back:
            return 0
        if front == self.n:
            return self.cardPoints[front]
        if back == 0:
            return self.cardPoints[back]

        l = self.cardPoints[front] + self.maxScoreHelper(k - 1, front + 1, back)
        r = self.cardPoints[back] + self.maxScoreHelper(k - 1, front, back - 1)
        result = max(l, r)

        return result


s = Solution()
cardPoints1, k1 = [1, 2, 3, 4, 5, 6, 1], 3  # Expected: 12
cardPoints2, k2 = [2, 2, 2], 2  # Expected: 4
cardPoints3, k3 = [9, 7, 7, 9, 7, 7, 9], 7  # Expected: 55
s.maxScore(cardPoints3, k3)
