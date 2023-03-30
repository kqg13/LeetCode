# Easy problem 922: Sort Array by Parity II

# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i]
# is even, i is even.


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_list = list(filter(lambda x: x % 2 == 0, A))
        odd_list = list(filter(lambda x: x % 2 == 1, A))

        return [val for pair in zip(even_list, odd_list) for val in pair]
