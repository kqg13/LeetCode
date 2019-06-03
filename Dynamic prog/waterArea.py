# Hard DP problem: Water Area
# You are given an array of ints. Each non-zero int represents the height of
# a pillar of width 1. Imagine water being poured over all of the pillars
# and return the surface area of the water trapped between the pillars viewed
# from the front. Note that spilled water should be ignored.

# Sample input: [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
# Sample output: 48


def waterArea(heights):
    if not heights:
        return 0

    # Set left and right to first non-zeroes
    for i, height in enumerate(heights):
        left = i
        if height != 0:
            break

    for i, height in enumerate(reversed(heights)):
        right = len(heights) - i - 1
        if height != 0:
            break

    pillars = 0  # May need to reset
    current = left + 1
    area = 0

    while current <= right:
        if heights[current] == 0:
            current += 1
            continue
        elif heights[current] < heights[left]:
            pillars += heights[current]
        else:
            length = heights[left]
            width = current - left - 1
            area += (length * width) - pillars
            # Reset
            pillars = 0
            left = current
        current += 1

    if left != right:
        current = right - 1
        pillars = 0
        while current >= left:
            if heights[current] == 0:
                current -= 1
                continue
            elif heights[current] < heights[right]:
                pillars += heights[current]
            else:
                length = heights[right]
                width = right - current - 1
                area += (length * width) - pillars
                # Reset
                pillars = 0
                right = current
            current -= 1

    return area


arr = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
# arr = [0, 8, 0, 0, 5, 0, 0, 10]
waterArea(arr)
