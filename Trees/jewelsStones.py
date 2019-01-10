# Easy Problem 771: Jewels and Stones


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


jis = Solution()
print(jis.numJewelsInStones("aA", "aAAbbbb"))
print(jis.numJewelsInStones("z", "ZZ"))
