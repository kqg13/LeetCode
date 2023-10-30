# 1763: Longest Nice Substring
# https://leetcode.com/problems/longest-nice-substring/description/

class Solution:
    def longestNiceSubstring(self, s):
        """
        s:string
        return: string
        """
        self.result = ""
        if len(s) > 1:
            self.longestNiceSubstringHelper(s)
        return self.result

    def longestNiceSubstringHelper(self, s):
        if len(s) < 2:
            return
        if len(s) == 2:
            if len(self.result) < 2:
                if (s[0].isupper() and s[0].lower() == s[1]) or (s[1].isupper() and s[1].lower() == s[0]):
                    self.result = s
            return

        mines_indexes = self.getMines(s)

        if not mines_indexes:
            if len(s) > len(self.result):
                self.result = s
            return

        # First call
        first_mine = mines_indexes[0]
        self.longestNiceSubstringHelper(s[0:first_mine])

        for mine in mines_indexes[1:]:
            self.longestNiceSubstringHelper(s[first_mine + 1:mine])
            first_mine = mine

        # Last call
        last_mine = mines_indexes[-1]
        self.longestNiceSubstringHelper(s[last_mine + 1:])

    def getMines(self, s):
        lower_set, upper_set, mines = set(), set(), list()

        for i, ch in enumerate(s):
            upper_set.add(ch) if ch.isupper() else lower_set.add(ch)

        for ch in upper_set:
            if ch.lower() not in lower_set: mines.append(ch)
        for ch in lower_set:
            if ch.upper() not in upper_set: mines.append(ch)

        # Get indexes
        indexes = [i for i, ch in enumerate(s) if ch in mines]
        return indexes
