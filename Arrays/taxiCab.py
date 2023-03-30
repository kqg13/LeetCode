# Variation of taxicab number (Hardy-Ramanujan) problem

# Return all numbers that can be expressed as a^3 + b^3 = c^3 + d^3 from
# 1 to N given some N

import math


def findTaxiCabs(n):
    results = []
    threshold = 1e-6
    for i in range(1, n + 1):
        if isTaxiCab(i, threshold):
            results.append(i)
    return results


def isTaxiCab(i, threshold):
    pairs = 0
    for a in range(1, math.ceil(cubeRoot(i / 2))):
        b_cubed = i - (a ** 3)
        b = cubeRoot(b_cubed)
        if abs(round(b) - b) < threshold:
            pairs += 1
            if pairs == 2:
                return True
    return False


def cubeRoot(x):
    return x ** (1. / 3)


print(findTaxiCabs(14000))
