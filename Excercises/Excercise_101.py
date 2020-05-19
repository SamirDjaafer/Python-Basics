# Define the following variables
# name, last_name, age, eye_color, hair_color

name = ''
last_name = ''
eye_color = ''
hair_color = ''
age = ''

# Prompt user for input and Re-assign these

name = input('So what name do you go by? ')
last_name = input('Fascinating, and what is your last name,' + ' ' + name + '? ')
eye_color = input('Ok,' + name + ' ' + last_name + '. What colour eyes do you have? ')
hair_color = input('What lovely hair you have, ' + name + '. What colour is it? ')
age = int(input('How old are you, ' + name + '? '))
birthday_passed = input('Has your birthday passed this year? Yes / No ')

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

print('Hello ' + name + '! Welcome, your age is ' + str(age) + ', your eyes are ' + eye_color + ' and your hair colour is ' + hair_color + '.')


#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

if birthday_passed == 'Yes':
    birthday_passed = 0
else:
    birthday_passed = 1

year_born = 2020 - age - birthday_passed

print('You said you were ' + str(age) + ' hence you were born in ' + str(year_born))

#Extra - Cast your input

#Done