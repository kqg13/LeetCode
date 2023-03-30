# 383: Ransom Note

# https://leetcode.com/problems/ransom-note/

# Given 2 strings ransomNote and magazine, return true if ransomNote can be constructed from magazine
# and false otherwise.  Each letter in magazine can only be used once in ransomNote.

from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rn_count = Counter(ransomNote)
        for c in magazine:
            if c in rn_count:
                rn_count[c] -= 1
        check = all(count <= 0 for count in rn_count.values())
        return check


s = Solution()
rn1, mag1 = "a", "b"
rn2, mag2 = "aa", "ab"
rn3, mag3 = "aa", "aab"
rn4, mag4 = "cat", "kencatalanjim"
s.canConstruct(rn1, mag1)
s.canConstruct(rn2, mag2)
s.canConstruct(rn3, mag3)
s.canConstruct(rn4, mag4)

