# Easy array problem 243: Shortest Word Distance

# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
#
# Example:
# Assume words = ["practice", "makes", "perfect", "coding", "makes"]
# Input: word1 = “coding”, word2 = “practice”
# Output: 3

# Input: word1 = "makes", word2 = "coding"
# Output: 1

import sys


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortest = w1_pos = w2_pos = sys.maxsize

        for i, word in enumerate(words):
            if word == word1:
                w1_pos = i
            elif word == word2:
                w2_pos = i
            else:
                continue
            shortest = min(shortest, abs(w1_pos - w2_pos))

        return shortest
