def amazonMinSort(arr):
    swaps = 0
    sortedArr = sorted(arr)
    idxLocations = generateLocations(arr)
    for i in range(len(arr)):
        targetVal = sortedArr[i]
        targetIdx = idxLocations[targetVal]

        if i != targetIdx:
            swaps += 1
            valToSwap = arr[i]
            idxLocations[valToSwap] = targetIdx
            arr[i], arr[targetIdx] = arr[targetIdx], arr[i]
    return swaps


def generateLocations(arr):
    idxLocations = {arr[i]: i for i in range(len(arr))}
    return idxLocations


def getInvCount(arr):
    inv_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


arr1 = [5, 1, 4, 2]
arr2 = [8, 4, 2, 1]
# print(amazonMinSort(arr1))
print(getInvCount(arr2))
