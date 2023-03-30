# Easy binary search problem 852: Peak Index in a Mountain Array

# Let's call an array A a mountain if the following properties hold:
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

# Given an array that is definitely a mountain, return any i such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example:
# Input: [0,2,1,0] Output: 1


class Solution:
    # Time: O(N)
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i

    # Time: O(logN)
    def peakIndexInMountainArrayBinary(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low, high = 0, len(A) - 1
        while low < high:
            mid = (low + high) // 2
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low
    
    def peakIndexInMountainArrayBin(self, A):
        peak = self.peakIndexInMountainArrayBinaryHelper(A, 0, len(A) - 1)
        return peak

    def peakIndexInMountainArrayBinaryHelper(self, A, low, high):
        mid = (low + high) // 2
        if low < high:
            if A[mid] < A[mid - 1]:
                return self.peakIndexInMountainArrayBinaryHelper(A, low, mid-1)
            elif A[mid] < A[mid + 1]:
                return self.peakIndexInMountainArrayBinaryHelper(A, mid + 1, high)
        return mid
