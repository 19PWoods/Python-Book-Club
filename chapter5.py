# # # If Statements
# cars = ['audi', 'bmw', 'subaru', 'toyota']

# # for car in cars:
# if car == 'bmw':
#     print(car.upper())
# else:
#     print(car.title())

# # Case sensitivity in Python
# car = 'Audi'
# print(car.lower() == 'audi')

# # Checking for inequality
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# age = 18
# print(age == 18)

# if age != 42:
#     print("That is not the correct answer!")

# print(age <= 45)
# print(age > 5 and age <= 23)
# print(age > 5 or age <= 23)

# # Checking Value is in list
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)

# # # Checking value IS NOT in list
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

# # Boolean Expressions
# game_active = True
# can_edit = False

# # # If statements
# age = 19
# if age > 18:
#     print("You can vote!")
#     print("Have you registered to vote?")

# # age = 17
# if age > 18:
#     print("\nYou can vote!")
#     print("Have you registered to vote?")
# else:
#     print("\nSorry, no voting for you!")
#     print("Please register as soon as you are 18!")

# age = 72
# if age < 4:
#     print("You are free admission!")
# elif age < 18:
#     print("Admission costs $25!")
# else:
#     print("Admission is $40!")

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"Your admission cost is ${price}.")

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:     # you can omit the else statement
#     price = 20

# print(f"Your admission cost is ${price}.")

# # Testing multiple conditions
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\n")

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")

# # Using if statements with lists
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# # for requested_toppings in requested_toppings:
# #     print(f"Adding {requested_toppings}.")
# # print("\nFinished making your pizza!")

# # for requested_toppings in requested_toppings:
# #     if requested_toppings == 'green peppers':
# #         print("Sorry, out of green peppers.")
# #     else:
# #         print(f"Adding {requested_toppings}.")
# # print("\nFinished making your pizza!")

# # requested_toppings = []
# # if requested_toppings:
# #     for requested_toppings in requested_toppings:
# #         print(f"Adding {requested_toppings}.")
# #     print("\nFinished making your pizza!")
# # else:
# #     print(f"Are you sure you want a plain pizza?.")

# # Using Multiple Lists
# available_toppings = ['mushrooms', 'olives',
#                       'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_toppings in requested_toppings:
#     if requested_toppings in available_toppings:
#         print(f"Adding {requested_toppings}.")
#     else:
#         print(f"Sorry, we don't have {requested_toppings}.")
# print("\nFinished making your pizza!")


# random.shuffle() randomly shuffles array values
# Example from Bob - Monty Carlo

import random

number_of_shots = 5
possible_alien_colors = ['red', 'orange',
                         'yellow', 'green', 'blue', 'black', 'violet']
points = 0
total_points = 0

user_input = input(
    "\n\nHow many simulations would you like to run? Simulations: ")
simulations = int(user_input)

for run_number in range(1, simulations+1):
    # print(run_number)
    for shot in range(1, number_of_shots+1):
        random.shuffle(possible_alien_colors)
        shot_down_color = possible_alien_colors[0]
        if shot_down_color == 'green':
            points = points + 5
        if shot_down_color == 'yellow':
            points = points + 10
        if shot_down_color == 'red':
            points = points + 15
        if shot_down_color == 'orange' or shot_down_color == 'blue' or shot_down_color == 'black' or shot_down_color == 'violet':
            points = points + 1
        # print(f"Shot {shot}: You shot a {shot_down_color} alien. You now have {points} points!")
    total_points = total_points + points
    points = 0
print(
    f"\nDone. After {simulations} runs you have a grand total of {total_points} points.")
average = total_points/simulations
print(f"That's an average of {average} points per game!")
