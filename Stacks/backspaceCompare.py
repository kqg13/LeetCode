# Easy problem 844: Backspace String Compare
from itertools import zip_longest


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_stack = []
        t_stack = []

        for letter in S:
            if s_stack and letter == "#":
                s_stack.pop()
            if letter != "#":
                s_stack.append(letter)

        for letter in T:
            if t_stack and letter == "#":
                t_stack.pop()
            if letter != "#":
                t_stack.append(letter)

        return s_stack == t_stack

    def betterbackspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in zip_longest(F(S), F(T)))


s = Solution()
S = "y#fo##f"
T = "y#f#o##f"
print(s.backspaceCompare(S, T))
print(s.betterbackspaceCompare(S, T))
