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

# input("Ok, done with that; let's move on. Press <enter> to continue\n")

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

# # Looping Through Dictionaries. Have to create two variable names
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

# # Looping Through Dictionary's Keys in Particular Order
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }


# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# print("\nThe following languages have been")
# for language in favorite_languages.values():
#     print(language.title())

# print("\nThe following languages have been")
# for language in set(favorite_languages.values()):
#     print(language.title())

# # Nesting - unrealisitc
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Nesting - realistic
# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print(f"Total number of aliens: {len(aliens)}")

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# # A list in a Dictionary (this is more efficient ram wise then a list of lists)
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print(f"You ordered a {pizza['crust']}-crust pizza"
#       " with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }
# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# # input() allows you to have user put in value. Always saves as str

# # ALWAYS USE .get() TO GET DATA OUT OF DICTIONARIES - don't uses the way the book tells you

# user_info = {}


# Sets will not allow for duplicates

# Dictionary in a dictionary...
# dictionaries defined...              NOTE: Be careful of the commas!
users = {
    'aeinstein':
    {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
        'mcurie':
    {
        'first': 'marie',
        'last': 'cury',
        'location': 'paris',
    },
        'pwoods':
    {
        'first': 'phil',
        'last': 'woods',
        'location': 'UMN',
    },
}

# # print it all out...
# for username in users.items():               # the top level...
#     print(f"{username}")


# print("\n-----\n")


# for username, users in users.items():        # another level...
#     print(f"{users['last']}")


# test_name = "bob"
# print(f"\n----- {test_name.title()} -----\n")  # making sure this works...


# for username, users in users.items():        # capitalize...  What!!!??  Why??
# print(f"{users['last'].title()}")
#

print("\n-----\n")


for username, extras in users.items():        # Another way... Argh! What's wrong here!
    for key, value in extras.items():
        lastname = extras['last']
        firstname = extras['first']
    print(f"One of the scientists: {firstname.title()} {lastname.title()}")
