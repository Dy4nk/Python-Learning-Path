"""
Day 02 - 20:08
Strings
"""

import os

os.system("cls")

my_string = "My string"
my_other_string = 'My other string'

print(len(my_string))
print(len(my_other_string))

print("\n" + my_string + " " + my_other_string)

my_newline_string = "\nThis string\ndoesn't follow the rules"
print(my_newline_string)

my_tab_string = "\nThis string\tdoesn't follow the rules either"
print(my_tab_string)

my_escape_string = "\n\tThis string\ndoesn't like tabulation"
print(my_escape_string)

# Formatting
name, age = "Dy4nk", 69
print("\nMy name is {} and I'm {} years old".format(name, age))
print("My name is %s and I'm %d years old" %(name, age))
print("My name is " + name + " and I'm " + str(age) + " years old")
print(f"My name is {name} and I'm {age} years old\n")

# Unpacking characters
lang = "Python"
a, b, c, d, e, f = lang
print(a)
print(b)
print(a)
print(b)
print(a)
print(b)

# Division
lang_slice = lang[1:3]
print("\n" + lang_slice)

lang_slice = lang[1:]
print(lang_slice)

lang_slice = lang[-2]
print(lang_slice)

lang_slice = lang[::-1]
print(lang_slice + "\n")

# Functions
print(lang.capitalize())
print(lang.upper())
print(lang.count("t"))
print("1".isnumeric())
print(lang.isnumeric())
print(lang.lower())
print(lang.upper().isupper())
print(lang.startswith("Py"))