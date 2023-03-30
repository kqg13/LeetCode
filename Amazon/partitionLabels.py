# LeetCode #763: Partition Labels / Amazon Practice Question #2

# You are given a string s. We want to partition the string into as many parts
# as possible so that each letter appears in at most one part.
# Return a list of integers representing the size of these parts.

from collections import Counter


class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        self.results = []
        table = self.createDict(s)
        return self.results

    def createDict(self, s):
        d = {c: i for i, c in enumerate(s)}
        return d

    def doPartition(self, s, d):
        startpoint = 0
        new_endpoint = d[s[startpoint]]

        while endpoint < len(s) - 1:
            new_endpoint = self.doPartitionNew(s, startpoint, endpoint, d)

            if new_endpoint == endpoint:
                self.results.append(endpoint - startpoint + 1)
                startpoint = endpoint + 1
                endpoint = d[s[startpoint]]
            else:
                new_endpoint = self.doPartitionNew(s, endpoint, new_endpoint, d)

    def doPartitionNew(self, s, startpoint, endpoint, d):
        charset = set()
        new_endpoint = endpoint
        for i in range(startpoint + 1, endpoint):
            charset.add(s[i])

        for c in charset:
            n = d[c]
            if n > endpoint:
                new_endpoint = n
        return new_endpoint


s = Solution()
s1 = "ababcbacadefegdehijhklij"
s.partitionLabels(s1)
