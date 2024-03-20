# Functions!!

# def greet_user():
#     """Display a simple greeting.""" # docstring, describes what the function does
#     print("Hello!")
# greet_user()

# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")


# greet_user('jesse')

# Try it yourself


# def display_message():
#     """Tell people what I am learning in boating school."""
#     print('We are learning about functions')


# display_message()


# def favorite_book(book):
#     """Tell me your favorite book!"""
#     print(f"One of my favorite books is {book}!")


# favorite_book('Harry Potter')

# # Passing arguements
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet('dog', 'Ruby')


# def describe_pet(pet_name, animal_type='dog'):  # order matters here
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet(pet_name='Ruby')

# Reture Values


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# # Making argument optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician2 = get_formatted_name('john', 'hooker', 'lee')
# print(musician2)

# Returning a Dictionary


# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person


# musician = build_person('jimi', 'hendrix')
# print(musician)


# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person


# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# Using functions within while loop


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying List in a Function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# slice notation makes copy of list to send to function
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Passing an Arbitrary number of arguments


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments


def make_pizza(size, *toppings):
    """Summarie the pizza we are about to make."""
    print(f"\nMaking a {size}-inche pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
