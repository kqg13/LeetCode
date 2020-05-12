# Hard array problem: Largest Range

# Write a function that takes in an array of ints and returns an array of
# length 2 representing the largest range of nums contained in the array. The
# first number in the output should be the first num in the range while the
# second num should be the last num in the range. A range of numbers is defined
# as a set of nums that come right after each other in the set of real ints.
# Note that the numbers do not need to be ordered or adjacent in the array in
# order to form a range. Assume there will be only be one largest range.

# Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# Sample output: [0, 7


def largestRange(array):
    d = {x: True for x in array}
    best_range = []
    best_length = 0
    for num in array:
        current_length = 0
        if not d[num]:
            continue
        lb = num - 1
        ub = num + 1
        while lb in d and d[lb]:
            d[lb] = False
            current_length += 1
            lb -= 1
        while ub in d and d[ub]:
            d[ub] = False
            current_length += 1
            ub += 1
        if current_length >= best_length:
            best_length = current_length
            best_range = [lb + 1, ub - 1]
    return best_range
