def partition(arr, low, high):
    pivot = high
    divider = low

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


lst = [6, 2, 3, 7]
quicksort(lst, 0, len(lst) - 1)
print(lst)
