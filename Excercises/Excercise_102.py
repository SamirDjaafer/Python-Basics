# Practice strings
# Welcome to Sparta - exercise

# Version 1 specs - with concatenation
# define a variable name, and assign a string
string = "Hello World! Yes.. very original"

# prompt the user for input and ask the user for his/her name
string = input("What is your name? ")
# re assign the original variable this this input

# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print(("Welcome to python, " + string).strip())
# Version 2 - with interpolation

# ask the user for a first name, save it in a variable
first_name = input('What is your first name? ')
# ask the user for a last name, save it in a variable
last_name = input('What is your last name? ')
# use interpolation to print the message
message = "So your full name is " + first_name + ' ' + last_name
print(message)

full_name = first_name + ' ' + last_name
# Calculate year of birth
# gather details on age and name
age = input('How old are you, ' + first_name + '? ')
birthday_gone = input('Has your birthday passed this year? Yes / No ')

if birthday_gone == 'Yes':
    birthday_gone = 0
else:
    birthday_gone = 1

birth_year = 2020 - int(age) - birthday_gone
# print something like
# OMG <person>, you are <age> years old so you were born in <year>
print("OMG " + full_name + ", you are " + age + " years old so you were born in " + str(birth_year))