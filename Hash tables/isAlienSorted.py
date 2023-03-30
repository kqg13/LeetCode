# 953. Verifying an Alien Dictionary

# In an alien language, surprisingly they also use english LC letters,
# but possibly in a different order. The order of the alphabet is some permutation of LC letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographicaly in this alien language.

# Examples:
# Input: words1 = ["hello", "leetcode"], order1 = "hlabcdefgijkmnopqrstuvwxyz" ---> true
# Input: words2 = ["word", "world", "row"], order2 = "worldabcefghijkmnpqstuvxyz" ---> false
# Input: words3 = ["apple", "app"], order3 = "abcdefghijklmnopqrstuvwxyz" ---> false


# Time: O(M) where M is total # of char in words, Space: O(1) because hashmap stores fixed 26 letters
class Solution:
    def isAlienSorted(self, words, order):
        """
        :param words: List[str]
        :param order: str
        :return: bool
        """
        alien_map = {letter: i for i, letter in enumerate(order)}
        n_words = len(words) - 1
        for i in range(n_words):
            current_word_length = len(words[i])
            for j in range(current_word_length):
                if j >= len(words[i + 1]):
                    return False

                current_word, next_word = words[i], words[i + 1]

                if current_word[j] != next_word[j]:
                    if alien_map[current_word[j]] > alien_map[next_word[j]]:
                        return False
                    break
        return True

    # Algorithm:
    # 1)    If all corresponding chars are the same but we've ran out of letters in next_word, then
    #       return False because next_word should come before current_word ('apple', 'app')
    #
    # 2)    If a corresponding char (current_word :: next_word) is sorted correctly, break
    #       out of loop and  go to next pair
    #
    # 3)    If something is unsorted, immediately return False


s = Solution()
words1, order1 = ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
words2, order2 = ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"
words3, order3 = ["apple", "app"], "abcdefghijklmnopqrstuvwxyz"
# print(s.isAlienSorted(words1, order1))
# print(s.isAlienSorted(words2, order2))
# print(s.isAlienSorted(words3, order3))
