# 205: Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t_map = dict()
        t_seen = set()

        for s_char, t_char in zip(s, t):
            if s_char not in s_t_map:
                if t_char not in t_seen:
                    s_t_map[s_char] = t_char
                else:
                    return False
            else:
                t_val = s_t_map[s_char]
                if t_char != t_val: return False

            t_seen.add(t_char)
        return True

