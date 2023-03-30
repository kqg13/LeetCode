# AlgoExperts Medium Array Problem: Monotonic Array

# Write a function that takes an array of ints and returns a bool representing
# whether the array is monotonic. An array is said to be monotonic if its
# elements, from left to right, are entirely non-increasing or entirely non-
# decreasing.


def isMonotonic(array):
    if len(array) == 0 or len(array) == 1:
        return True
    return isDecreasing(array) or isIncreasing(array)


def isDecreasing(array):
    return all(array[i] <= array[i-1] for i in range(1, len(array)))


def isIncreasing(array):
    return all(array[i] >= array[i-1] for i in range(1, len(array)))


arr1 = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
arr2 = [10, 2, 1, 3]
arr3 = [-100, -1, 0, 0, 1]
print(isMonotonic(arr1))
print(isMonotonic(arr2))
print(isMonotonic(arr3))

