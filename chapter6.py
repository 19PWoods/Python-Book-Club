# # Dictionaries {}: collection of key-value pairs (where key = value)

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# alien_0['x position'] = 0
# alien_0['y position'] = 25
# print(alien_0)

# # Starting with an empty dictionary
# alien_1 = {}
# alien_1['color'] = 'blue'
# alien_1['points'] = 50
# print(alien_1)

# # Modifying values in dictionary
# print(f"The alien is {alien_0['color']}")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")

# alien_0['speed'] = 'medium'
# print(alien_0)
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien
#     x_increment = 3

# alien_0['x position'] = alien_0['x position'] + x_increment
# print(alien_0['x position'])

# # Removing Key-Value Pairs
# del alien_0['points']
# print(alien_0)

# # Dictionary of Similar Objects (can use space for dicts)
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'r',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# # Using get() to Acess Values
# alien_0 = {'color': 'green', 'speed': 'slow'}
# # print(alien_0['points'])  # gives you error

# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# # Try it yourself 6.1-6.3
# phil = {
#     'first name': 'Philip',
#     'last name': 'Woods',
#     'age': '26',
#     'city': 'St. Paul',
#     'occupation': 'Student',
# }
# print(phil)

# fav_numbers = {
#     'Phil': 18,
#     'Mari': 12,
#     'Bob': 17,
#     'Aspen': 21,
#     'Olivia': 666,
# }

# Looping Through Dictionaries. Have to create two variable names
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'r',
# }
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# # Looping Through All Keys in a Dictionary
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'r',
# }
# for name in favorite_languages.keys():
#     print(name.title())

# for name in favorite_languages:  # does same as above
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'eren' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# Looping Through Dictionary's Keys in Particular Order
# End on page 2
