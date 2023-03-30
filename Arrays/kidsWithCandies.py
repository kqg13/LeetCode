# Array problem #1431; Kids With the Greatest Number of Candies

# Given the array candies and the integer extraCandies, where candies[i]
# represents the number of candies that the ith kid has.
# For each kid check if there is a way to distribute extraCandies among the
# kids such that he or she can have the greatest number of candies among them.
# Notice that multiple kids can have the greatest number of candies.
#
#  Ex. 1: Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
#         Output: [true, true, true, false, true]

#  Ex. 2: Input: candies = [4, 2, 1, 1, 2], extraCandies = 1
#         Output: [true, false, false, false, false]

#  Ex. 3: Input: candies = [12, 1, 12], extraCandies = 10
#         Output: [true, false, true]


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        results = []
        for i, candy in enumerate(candies):
            candies[i] += extraCandies
            results.append(True) if candies[i] == max(candies) else results.append(False)
            candies[i] -= extraCandies
        return results

    def kidsWithCandiesBetter(self, candies, extraCandies):
        results = []
        best = max(candies)
        possible = best - extraCandies
        for candy in candies:
            results.append(True) if candy >= possible else results.append(False)
        return results


s = Solution()
c1, ec1 = [2, 3, 5, 1, 3], 3
c2, ec2 = [4, 2, 1, 1, 2], 1
c3, ec3 = [12, 1, 12], 10
s.kidsWithCandiesBetter(c1, ec1)
s.kidsWithCandiesBetter(c2, ec2)
s.kidsWithCandiesBetter(c3, ec3)
