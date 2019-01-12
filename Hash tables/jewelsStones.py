# Easy Problem 771: Jewels and Stones


# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.  Each character in S is a type of
# stone you have.  You want to know how many of the stones you have are also
# jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are
# letters. Letters are case sensitive, so "a" is considered a different type
# of stone from "A".

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        this_dict = {}
        for jewel in J:
            this_dict[jewel] = 1
        for stone in S:
            if stone in this_dict:
                count += 1
        return count
