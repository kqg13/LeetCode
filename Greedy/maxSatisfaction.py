# 1402: Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/description/

class Solution:
    def maxSatisfaction(self, satisfaction):
        """
        satisfaction: List[int]
        return: int
        """
        sorted_satisfactions = sorted(satisfaction)
        positives = [num for num in sorted_satisfactions if num >= 0]
        sum_of_positives = sum(positives)

        if sum_of_positives == 0: return 0

        result = sum([(i+1) * num for i, num in enumerate(positives)])

        smallest_neg_index = 0
        for i, num in enumerate(sorted_satisfactions):
            if num >= 0:
                smallest_neg_index = i - 1
                break

        for i in range(smallest_neg_index, -1, -1):
            sum_of_positives += sorted_satisfactions[i]
            if sum_of_positives > 0:
                result += sum_of_positives
            else:
                break

        return result


s = Solution()
s1 = [-1, -8, 0, 5, -9]  # Expected: 14
s2 = [-1, -4, -5]  # Expected: 0
s3 = [2, -2, -3, 1]  # Expected: 6
s4 = [-5, -7, 8, -2, 1, 3, 9, 5, -10, 4, -5, -2, -1, -6]  # Expected: 260
