import random


def partition(arr, low, high):
    pivot = random.randint(low, high)  # random pivot (remove lines 5-6 for high as pivot)
    arr[high], arr[pivot] = arr[pivot], arr[high]
    pivot = high
    divider = low  # whatever before divider is less than the pivot

    for i in range(low, high):
        if arr[i] < arr[pivot]:
            arr[i], arr[divider] = arr[divider], arr[i]
            divider += 1
    arr[pivot], arr[divider] = arr[divider], arr[pivot]
    return divider


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


lst = [3, 1, 2, 5, 4, 6, 9, 7, 10, 8]
quicksort(lst, 0, len(lst) - 1)
print(lst)
print(str(18.95 + 40.88 + 16.72 + 4.98))
