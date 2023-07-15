"""
Day 02 - 21:47
Lists
"""

import os

os.system("cls")

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [69, 1.70, "Dy4nk"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[1])
print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))

age, height, name = my_other_list # If not all elements inside lists are unpacked, it will give an error.
print(age)

print(my_list + my_other_list)