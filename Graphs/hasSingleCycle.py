# Single Cycle Check: Graph Problem

# You are given an array of ints. Each int represents a jump of its val in the
# array. For instance, the int 2 represents a jump of 2 indices forward in
# the array; the int 3 represents a jump of 3 indices backward.
# If a jump spills past the array's bounds, it wraps to the other side.
# Similarly, a jump of 1 at the last index in the array brings us to index 0.
# Write a function that returns a bool representing whether the jumps in the
# array form a single cycle. A single cycle occurs if, starting at any index
# and following the jumps, every element is visited exactly once before landing
# back on the starting index.


# Sample input: [2, 3, 1, -4, -4, 2], Sample output: True

# Time: O(N), Space: O(N)
def has_single_cycle(array):
    current_idx, array_len = 0, len(array)
    d = {}
    cycle = False

    while not cycle:
        d[current_idx] = True
        jump = array[current_idx]
        current_idx = (current_idx + jump) % array_len
        if current_idx in d:
            cycle = True

    if len(d) == array_len and current_idx == 0:
        return True
    return False


arr = [2, 3, -2, -4, -4, 2]
has_single_cycle(arr)