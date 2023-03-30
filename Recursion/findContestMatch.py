# Medium Recursion Problem 544: Output Contest Matches

# During the NBA playoffs, we always arrange the rather strong team to play with
# the rather weak team, like make the rank 1 team play with the rank nth team, which
# is a good strategy to make the contest more interesting. You're given n teams, and
# need to output their final contest matches in the form of a string.
#
# The n teams are given in the form of pos integers from 1 to n, which represents
# their initial rank. (Rank 1 is the strongest team and Rank n is the weakest)

# We'll use parentheses('(', ')') and commas(',') to represent the contest team
# pairing - parentheses('(' , ')') for pairing and commas(',') for partition.

# Example 1: Input: 2, Output: (1, 2)
# Example 2: Input: 4, Output: ((1,4),(2,3))
# Example 3: Input: 8, Output: (((1,8),(4,5)),((2,7),(3,6)))


class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        teamList = list(map(str, [i for i in range(1, n + 1)]))
        while len(teamList) > 1:
            n = int(len(teamList) / 2)
            print(n, teamList)
            for i in range(0, n):
                teamList[i] = '({},{})'.format(teamList[i], teamList.pop())
        return teamList[0]


s = Solution()
print(s.findContestMatch(8))
