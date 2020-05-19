import time
# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
menu = ['Pizza','Burger','Pasta','Soup','Lasagne']
food_order = []

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
food_order.append(input('So what would you like to eat? '))
food_order.append(input('Anything else with that? '))
food_order.append(input('Good choices. Would you like anything else? '))

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.
print("That's enough food for you I think. Im just going to repeat your order back to you.")
time.sleep(2)
print("So you first chose the " + food_order[0] + ", then you ordered the " + food_order[1] + ", followed by the " + food_order[2] + ".")

# starter code
# menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
# food_order = []

# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything

for item in food_order:
    print(item.capitalize())