# 890: Find and Replace Pattern
# https://leetcode.com/problems/find-and-replace-pattern/


class Solution:
    def __init__(self):
        self.pattern = None

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        self.pattern = pattern
        result = [word for word in words if self.isValid(word)]
        return result

    def isValid(self, word):
        word_dict = dict()
        pattern_set = set()

        for w, p in zip(word, self.pattern):
            if w not in word_dict:
                if p in pattern_set:
                    return False
                else:
                    word_dict[w] = p
                    pattern_set.add(p)
            else:
                val = word_dict[w]
                if val != p:
                    return False
        return True
