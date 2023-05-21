# 763: Partition Labels
# https://leetcode.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_dict = self.createLastIndexMap(s)
        start, max_last = 0, 0
        results = list()
        for i, char in enumerate(s):
            max_last = max(max_last, last_dict[char])
            if max_last == i:
                results.append(max_last - start + 1)
                start = i + 1
        return results

    def createLastIndexMap(self, s):
        d = {char: i for i, char in enumerate(s)}
        return d


sol = Solution()
s1 = "ababcbacadefegdehijhklij"  # Expected: [9, 7, 8]
s2 = "eccbbbbdec"  # Expected: [10]
s3 = "ab"  # Expected: [1, 1]
