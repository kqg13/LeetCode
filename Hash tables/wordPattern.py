# 290: Word Pattern
# https://leetcode.com/problems/word-pattern/

from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()

        if len(pattern) != len(s_split): return False

        p_map, s_map = defaultdict(str), defaultdict(str)

        for i in range(len(pattern)):
            pattern_letter, s_word = pattern[i], s_split[i]

            if pattern_letter not in p_map and s_word not in s_map:
                p_map[pattern_letter] = s_word
                s_map[s_word] = pattern_letter
            else:
                p_word = p_map[pattern_letter]
                s_pattern = s_map[s_word]

                if p_word != s_word: return False
                if s_pattern != pattern_letter: return False
        return True


s = Solution()
pattern1, s1 = "abba", "dog cat cat dog"
pattern2, s2 = "abba", "dog cat cat fish"
pattern3, s3 = "aaaa", "dog cat cat dog"
pattern4, s4 = "abba", "dog cat cat cat"
pattern5, s5 = "abbx", "dog cat cat dog"
