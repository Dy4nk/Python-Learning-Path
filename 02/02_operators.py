"""
Day 02 - 18:38
Operators
"""

# Basic operators
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print("")

# Advanced operators
print(10 % 3)
print(10 // 3)
print(10 ** 3)
print("")

# Operators with strings
print("Slim " + "Shady")
print("")

'''
Invalid operators

print("Slim" - "Shady")
print("Slim" * "Shady")
print("Slim" / "Shady")
print("Slim" + 313666744)
print("Slim" * 2.5)
...
'''

# Operators with multiple types
print("Slim " + str(313666744)) # print("Slim" + "313666744")
print("Chika " * 2)
print("Chika " * (4 ** 2))
print("Chika " * (int(10 / 5)))
print("")

# Comparative operators
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print("")

print("Slim" > "Shady") # Alphabetical order (ASCII)
print(len("Slim") < len("Shady")) # Amount of chars
print("Slim" >= "Shady")
print("Slim" <= "Shady")
print("Slim" == "Shady")
print("Slim" != "Shady")

# Logical operators
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))
