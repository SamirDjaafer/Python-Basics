age = input('How old are you? ')
driver_license = input('Do you have a drivers license? Yes / No ')

if driver_license == 'Yes' or driver_license == 'yes':
    driver_license = True
else:
    driver_license = False


# - You can vote and drive
if int(age) >= 18 and driver_license == True:
    print('Nice, you can vote and drive')
# - You can vote
elif int(age) >= 18:
    print('You can vote!')
# - You can drive
elif driver_license == True:
    print('You can drive!')
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
elif int(age) >= 16 and int(age) < 18:
    print("you can't legally drink but your mates/uncles might have your back")

# - Your too young, go back to school!
elif int(age) < 16:
    print("You're too young, go back to school!")

 #  as a user I should be able to keep being prompted for input until I say 'exit'