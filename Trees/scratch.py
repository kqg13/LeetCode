# import math

lst = [1, 2, 3, 4, 5]
print(len(lst))
print(lst)
lst2 = lst
lst2.pop()
print(lst2)
print(lst)
# mid = size / 2 if size % 2 == 0 else math.ceil(size / 2)
print(5//2)
# print(lst[len(lst) / 2])
# str = "Kedar"
# print(str[-3::-1])
print("-2".isdigit())

S = [3, 2]
T = [2, 3]
print(S == T)
print(S.index(3))

if S[0] > S[1]:
    S[0], S[1] = S[1], S[0]
print(S)

x, y = 2, 3
print(x, y)

# Stack problem 496: Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/discuss/129745/fast-python-solution-0(n)
