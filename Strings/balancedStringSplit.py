# String problem 1221: Split a String in Balanced Strings

# Balanced strings are those who have equal quantity of 'L' and 'R' chars.
# Given a balanced string s split it in the max amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Ex. 1: s1 = "RLRRLLRLRL" --> 4
# Ex. 2: s2 = "RLLLLRRRLR" --> 3
# Ex. 3: s3 = "LLLLRRRR" --> 1
# Ex. 4: s4 = "RLRRRLLRLL" --> 2


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rCount, sCount, result = 0, 0, 0
        for letter in s:
            if letter == 'R':
                rCount += 1
            else:
                sCount += 1
            if rCount == sCount:
                result += 1
                rCount, sCount = 0, 0
        return result
