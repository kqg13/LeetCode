# 1524: Number of Sub-arrays With Odd Sum
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# https://www.youtube.com/watch?v=y949LlE29qQ

# Given an array of ints arr, return the # of subarrays with an odd sum.
# Since the answer can be very large, return it modulo 10^9 + 7.

# Goal: count the # of subarrays that sum to 1 in transformed array
# dp_one[i] = # of subarrays starting at i that sum to 1
# dp_one[0] = # of subarrays starting at i that sum to 0


# O(N)
class Solution:
    def numOfSubarrays(self, arr) -> int:
        n = len(arr)
        mod_val = 0, 10**9 + 7
        self.dp_one, self.dp_zero = [0] * n, [0] * n
        adj_arr = [i % 2 for i in arr]
        if n > 0:
            self.doBaseCase(adj_arr, n)
            for i in range(n - 2, -1, -1):
                if adj_arr[i] == 1:
                    self.dp_one[i] = 1 + self.dp_zero[i + 1]
                    self.dp_zero[i] = self.dp_one[i + 1]
                else:
                    self.dp_one[i] = self.dp_one[i + 1]
                    self.dp_zero[i] = 1 + self.dp_zero[i + 1]
        count = sum(self.dp_one)
        print(count)
        return count

    def doBaseCase(self, adj_arr, n):
        if adj_arr[n - 1] == 1:
            self.dp_one[n - 1] = 1
        if adj_arr[n - 1] == 0:
            self.dp_zero[n - 1] = 0


s = Solution()
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
arr3 = [1, 2, 3, 4, 5, 6, 7]
arr4 = [1, 3, 3, 5]
arr5 = [3, 5, 7]
s.numOfSubarrays(arr5)
