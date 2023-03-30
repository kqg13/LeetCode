# String problem #1119: Remove Vowels from a String

# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it,
# and return the new string.


class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels, removed = ['a', 'e', 'i', 'o', 'u'], ''
        for letter in S:
            if letter not in vowels:
                removed += letter
        return removed
