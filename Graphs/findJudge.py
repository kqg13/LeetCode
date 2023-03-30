# Graph Problem 997: Find the Town Judge

# In a town, there are N people labelled from 1 to N.  There is a rumor that one
# of these people is secretly the town judge. If the town judge exists, then:
#
# 1.    The town judge trusts nobody.
# 2.    Everybody (except for the town judge) trusts the town judge.
# 3.    There is exactly one person that satisfies properties 1 and 2.
#
# You are given trust, an array of pairs trust[i] = [a, b] representing that the
# person labelled a trusts the person labelled b.  If the town judge exists and
# can be identified, return the label of the town judge.  Otherwise, return -1.

# Example 1: Input: N = 2, trust = [[1, 2]] Output: 2
# Example 2: Input: N = 3, trust = [[1, 3], [2, 3], [3, 1]] Output: -1
# Example 3: Input: N = 3, trust = [[1, 3], [2, 3]] Output: 3
# Example 4: Input: N = 4, trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4,  3]] Output: 3

from collections import Counter


class Solution:
    def findJudge(self, n, trust) -> int:
        set_a = set([i for i in range(1, n + 1)])
        counter = Counter([b for a, b in trust])
        print(counter)
        for a, b in trust:
            try:
                set_a.remove(a)
            except:
                continue
        if len(set_a) == 1 and counter[list(set_a)[0]] == n - 1:
            return set_a.pop()
        else:
            return -1


s = Solution()
trust1 = [[1, 2]]
trust2 = [[1, 3], [2, 3], [3, 1]]
trust3 = [[1, 3], [2, 3]]
trust4 = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(s.findJudge(3, trust3))
