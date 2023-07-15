"""
Day 03 - 15:02
Tuples
"""

import os

os.system("cls")

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (69, 1.70, "Dy4nk", "Dy4nk")
my_other_tuple = (35, 60, 30, 29, 12)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Dy4nk"))
print(my_tuple.index(69))
print(my_tuple.index("Dy4nk"))

# my_tuple[1] = 1.90 Tuples don't support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple.insert(1, "Chika chika")
my_tuple[0] = 420
print(tuple(my_tuple))