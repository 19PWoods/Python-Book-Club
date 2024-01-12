# Inputs within coding

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you share your name, we can personalize the message you see."
# prompt += "\nWhat is your first name?"

# name = input(prompt)
# print(f"\nHello, {name}!")

# # Using int() to Accept Numerical Input
# age = int(input("How old are you? "))
# print(age)
# print(age >= 18)

# height = int(input("How tall are you, in inches? "))
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# # The modulo operator (tells you the remainder)
# print(4 % 3)
# print(5 % 3)
# print(6 % 3)
# print(7 % 3)

# number = int(input("Ente a nmber, and I'll tell you if it's even or odd: "))
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# # Introducing while Loops
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# # Using a Flag
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# # Using a break
# prompt = "\nPlease eneter the name of a city you have visited: "
# prompt += "\nEnter 'quit' to end the program."

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

# # Using continue in a Loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


# # ASCHII characters
# growing_string = ""
# for number in range(32, 127):
#     growing_string = growing_string + chr(number)
# print(f"{growing_string}\n")

# pg. 116 modulo...  which is pretty straight-forward

# Here's a challenge for everyone over break...
# Use the modulo operator to identify the first 100 prime numbers.
# Prime "rules"
#  • prime numbers are only divisible by themselves and 1
#  • prime numbers must be divisible by 2 numbers only (itself and 1)
# 1 is divisible by itself only, which is 1, so it is NOT prime
# 2 is divisible by itself and 1
# 3 is divisible by itself and 1
# 5 is divisible by itself and 1
# 7 is prime
# 11 is prime
# Note: every integer is divisible by 1, so this condition does not have to be tested

import numpy
prime_numbers = []
num = 2
division = list(range(2, 11))
remainders = []
for value in division:
    remainders.append(num % value)
# print(remainders)
# print(f"The product of the remainders is {numpy.prod(remainders)}!")
if numpy.prod(remainders) != 0:
    prime_numbers.append(num)
print(prime_numbers)
# print(remainders)

# print(division)
