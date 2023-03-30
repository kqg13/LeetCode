# Easy binary search 744: Find Smallest Letter Greater Than Target

# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter target, find the smallest element in the list that
# is larger than the given target.
#
# Letters also wrap around.  For example, if the target is target = 'z' and
# letters = ['a', 'b'], the answer is 'a'.


from bisect import bisect


class Solution:
    # Time: O(NlogN)
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low, high = 0, len(letters) - 1
        mid = (low + high) // 2

        if letters[mid] <= target:
            low = mid
            for i in range(low, high + 1):
                if letters[i] > target: return letters[i]
        elif letters[mid] >= target:
            high = mid + 1
            for i in range(low, high):
                if letters[i] > target: return letters[i]

        return letters[0]

    # Time: O(NlogN)
    def nextGreatestLetterBisect(self, letters, target):
        insert_pos = bisect(letters, target)
        return letters[insert_pos % len(letters)]
