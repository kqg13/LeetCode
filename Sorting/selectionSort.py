# Naive Implementation of Selection Sort


def selection_sort(arr):
    n = len(arr)
    n_swaps = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        # Swap
        arr[min_index], arr[i] = arr[i], arr[min_index]
        n_swaps += 1
    print(n_swaps)
    return arr


arr1 = [5, 1, 4, 2]
arr2 = [3, 7, 1, 2]
arr3 = [8, 4, 2, 1]
# print(selection_sort(arr1))
print(selection_sort(arr2))
# print(selection_sort(arr3))
