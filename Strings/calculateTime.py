# String problem #1165: Single-Row Keyboard

# There is a special keyboard with all keys in a single row. Given a string
# keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
# initially your finger is at index 0. To type a character, you have to move your
# finger to the index of the desired character. The time taken to move your finger
# from index i to index j is |i - j|.
#
# You want to type a string word. Write a function to calculate how much time it
# takes to type it with one finger.

# Ex 1: Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba" --> 4
# Ex 2: Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode" --> 73


class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        theDict = {letter: i for i, letter in enumerate(keyboard)}
        start, value, result = 0, 0, 0
        for letter in word:
            value = theDict[letter]
            result += abs(start - value)
            start = value
        return result
