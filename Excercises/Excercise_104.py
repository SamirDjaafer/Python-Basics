import random
# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# We should define/assign number to a variable called magic_number. We have imported 'random' and assigning a random int between 0 and 10
magic_number = random.randint(0,10)

# I need to ask user for input
your_number = int(input('Choose a number between 0 and 10 '))

# I need to check if this input matches a magic_number
if magic_number == your_number:
    print("What are the chances.. You was correct. Self five!")
else:
    print("Nope! That's not it.")

print("You selected " + str(your_number))
print("The magic number was " + str(magic_number))
# I need to let the user know if the response was write or not
#self five