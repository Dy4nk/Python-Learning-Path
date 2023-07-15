"""
Some variables
Not that interesting
"""

my_name = 'Chika chika Slim Shady'
print(my_name)

my_int = 313666744
print(my_int)

my_int_to_str = str(my_int)
print(my_int_to_str)
print(type(my_int_to_str))

my_bool = False
print(my_bool)

print(my_name, my_int, my_bool)

# DAY 2

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("This is of value:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("My name is:", name, surname, ". My age is:",
      age, ". And my alias is:", alias)

name = input("What's your name? ")
age = input('How old are you? ')
print(name)
print(age)

name = 35
age = "Brais"
print(name)
print(age)

address: str = "My address"
address = True
address = 5
address = 1.2
print(type(address))