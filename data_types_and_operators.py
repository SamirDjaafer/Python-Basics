# Including an apostrophe in a string

string = 'Samir\'s String'

print(string)

hw = "hello world"

print(hw[0:5])

# Removing White Space from a String

white_space = "String with space         "

print(len(white_space))

print(len(white_space.strip()))

# Some more methods

example_text = "some example text here here"

print(example_text.count("here"))

print("this returns 2 because 'here' appears twice")

# Bringing a string to lower case

example_text.lower()

print("The 'lower()' function converts a string to lower case")

# Bringing a string to upper case

example_text.upper()

print("The 'upper()' function converts a string to upper case")

# Capitalizing the first letter of each word in a string

string_cap = "the first letter from each word should be upper case"

print(string_cap.capitalize())

print("The 'capitaize()' method makes the first letter of each word capital within a string")

# Replacing text within a string

my_string = "this string is good"

print(my_string.replace('good','fantastic'))

# Concatination and Casting

x = 2
y = 5.4
z = " theres now a number 25.4 unless we put a space in"

print(str(x) + str(y) + z)

# Small task set by Shahrukh

g = "6"
print(type(g))
print(int(g))
print(float(g))

# Boolean operators

a = True
b = False

#

greetings = "Hello World!"

print(greetings.startswith("H"))

print(greetings.endswith("!"))

# What is a list? A list is a list.
# They are organized with indexes starting at 0

# Here we are creating a list and assigning it to a variable

my_stingy_landlords = ["Alfredo", "Betty", "Joanna", "Mr. Summersbee"]

print(my_stingy_landlords[2])

print(my_stingy_landlords)

my_stingy_landlords.append("Filipe Paiva")

print(my_stingy_landlords)

my_stingy_landlords.pop(3)

print(my_stingy_landlords)


