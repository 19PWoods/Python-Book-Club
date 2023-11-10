# For Loops
# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#     print(magician)

# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print("Thank you, everyone. That was a great magic show!")

# for value in range(1, 5):
#     print(value)

# for value in range(25):
#     print(value)

# numbers = list(range(6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
#     # square = value ** 2
#     # squares.append(square)

# print(squares)

# # Simple Statistics with List Numbers
# digits = list(range(0, 10))
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# # List comprehension: For loops in one line of code
# squares = [value**2 for value in range(1, 11)]
# print(squares)

# # Slicing a list: Accessing certain index of a list
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])  # automatically starts at beginning
# print(players[2:])
# print(players[-3:])

# # Looping through a slice
# print("Here are the first players on my team:")
# for player in players[:3]:  # looping only through first three players
#     print(player.title())

# # Copying a list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print(my_foods)
# print(friend_foods)

# # friend_foods = my_foods (this does not work, Python reads this as same list)

# Defining a tuple - use () instead of []
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 this does not work, you can't change a tuple!!
# in order to modify a tuple you must change the entire tuple
print("Original dimensions")
for dimension in dimensions:
    print(dimensions)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimensions)
