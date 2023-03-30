# Easy problem 905: Sort Array by Parity


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # Filter takes in a function and a list as arguments
        even_list = list(filter(lambda x: (x % 2 == 0), A))
        odd_list = list(filter(lambda x: (x % 2 == 1), A))
        return even_list + odd_list

    def sortWithComparator(self, A):
        A.sort(key=lambda x: x % 2)
        return A
        # you can't return A.sort() in 1 line because list.sort sorts
        # list in place

    def QuicksortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A


s = Solution()
A = [3, 1, 2, 4]
print(s.sortArrayByParity(A))
print(s.sortWithComparator(A))
print(s.QuicksortArrayByParity(A))
