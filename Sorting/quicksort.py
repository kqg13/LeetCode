import random


def partition(arr, low, high):
    # pivot = random.randint(low, high)  # random pivot (remove lines 5-6 for high as pivot)
    # arr[high], arr[pivot] = arr[pivot], arr[high]
    pivot = high
    divider = low  # whatever before divider is less than the pivot
    for i in range(low, high):
        if arr[i] < arr[pivot]:
            arr[i], arr[divider] = arr[divider], arr[i]
            divider += 1
    arr[pivot], arr[divider] = arr[divider], arr[pivot]
    # print("hello")
    return divider


def quicksort(arr, low, high):
    if low < high:  # means there are 2 elements at least
        print(arr)
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


lst1 = [3, 1, 2, 5, 4, 6, 9, 7, 10, 8]
lst2 = [2, 7, 1, 3]
lst3 = [5, 1, 4, 2]
lst4 = [3, 1, 2]
lst5 = [3, 1, 2, 5, 4, 6, 9, 12, 0, 8]
quicksort(lst5, 0, len(lst5) - 1)

# [3, 1, 2, 5, 4, 6, 0, 12, 9, 8]
# [3, 1, 2, 5, 4, 6, 0, 8, 9, 12]
