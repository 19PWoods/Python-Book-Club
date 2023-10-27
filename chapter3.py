# Introducing Lists

# Lists in Python are indicated by []
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1])  # special syntax to access last

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)


# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)


# Adding Elements to a list
motorcycles.append('ducati')
print(motorcycles)

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

motorcycles.insert(0, 'batman')
print(motorcycles)


# Removing Elements from a List
# del motorcycles[0]
# print(motorcycles)

# popped_motorcycles = motorcycles.pop()  # removes last item from list
# print(motorcycles)
# print(popped_motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owened was a {first_owned.title()}")

too_expensive = motorcycles.remove('ducati')
print(motorcycles)


# Organizing a list using sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("Here is the original list")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print(cars.reverse())

# Finding length of list
print(len(cars))  # do I have to put print everytime?
