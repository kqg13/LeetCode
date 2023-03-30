# Easy hash table problem 760: Find Anagram Mappings

# Given two lists A and B, and B is an anagram of A. B is an anagram of A
# means B is made by randomizing the order of the elements in A.
# We want to find an index mapping P, from A to B. A mapping P[i] = j means the
# ith element in A appears in B at index j.

# These lists A and B may contain duplicates. If there are multiple answers,
# output any of them.

# For example, given:
# A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]
# We should return [1, 4, 3, 2, 0]


class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        b_dict = {num: i for i, num in enumerate(B)}
        output = [b_dict[num] for num in A]
        return output
