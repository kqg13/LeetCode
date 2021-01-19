# LeetCode problem 1306: Jump Game III

# Given an array of non-negative ints, you are initially positioned at start
# index of array. When you are at index i, you can jump to i + arr[i] or i - arr[i],
# check if you can reach to any index with value 0.

# You can not jump outside of the array at any time.

# Examples:

# arr1 = [4, 2, 3, 0, 3, 1, 2], start = 5 ---> True
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3

# arr2 = [4, 2, 3, 0, 3, 1, 2], start = 0 ---> True
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3

# arr3 = [3, 0, 2, 1, 2], start = 2 ---> False
# Explanation: There is no way to reach at index 1 with value 0.


# Time: O(N), Space: O(N)
class Solution:
    def canReach(self, arr: list, start: int) -> bool:
        visited = [0] * len(arr)
        return self.canReachHelper(arr, start, len(arr) - 1, visited)

    def canReachHelper(self, arr, index, n, visited):
        if index > n or index < 0 or visited[index] == 1:
            return False
        visited[index] = 1
        if arr[index] == 0:
            return True
        
        newPlusIndex, newMinusIndex = index + arr[index], index - arr[index]

        plus = self.canReachHelper(arr, newPlusIndex, n, visited)
        minus = self.canReachHelper(arr, newMinusIndex, n, visited)
        return plus or minus


s = Solution()
arr1, start1 = [4, 2, 3, 0, 3, 1, 2], 5
arr2, start2 = [4, 2, 3, 0, 3, 1, 2], 0
arr3, start3 = [3, 0, 2, 1, 2], 2
arr4, start4 = [1, 2, 3], 3

print(s.canReach(arr1, start1))
print(s.canReach(arr2, start2))
print(s.canReach(arr3, start3))

