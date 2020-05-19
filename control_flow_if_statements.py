import time

# Control flow dictates where the code will run

# In coding we do this with if statements and while loops

# If statements work with booleans. True or False
# We usually use comparison operators <, <=, >, >=, ==

# is_rainy = True
#
# if is_rainy:
#     time.sleep(2)
#     print('Remember your umbrella!')

# weather = 'Sunny'
#
# if weather == 'Rainy':
#     print("Bring Umbrella!")
# elif weather == 'Sunny':
#     print("Put on lotion")
# elif weather == 'Stormy':
#     print("Stay safe at home!")

weather = input('What is the weather like today? ')

if weather == 'Rainy':
    print("Bring Umbrella!")
elif weather == 'Sunny':
    print("Put on lotion")
elif weather == 'Stormy':
    print("Stay safe at home!")

# Logical and is where both sides of the 'and' must equal to true in order for the statement to be accepted as true
# Logical or is where only one side of the 'or' must equal to true in order for the statement to be accepted as true



