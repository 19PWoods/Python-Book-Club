print('Hello Python world')

message = 'Hello Python World!'
print(message)

message = 'Hello Python Crash Course World!'
print(message)

# Method using dot (.) notation
name = "ada lovelace"
print(name.title())  # title case, starts every word with capital
print(name.upper())
print(name.lower())

# Using variables in strings
first_name = 'ada'
last_name = 'lovelace'
fullname = f"{first_name} {last_name}"
print(fullname)
print(f"Hello, {fullname.title()}!")

# Adding whitespaces
print('\tPython')  # adding tab
print("Languages:\nPython\nR\nJavaScript")  # adding new lines

favorite_language = 'python '
print(favorite_language)
# rstrip, lstrip, strip removes extra whitespaces
print(favorite_language.rstrip())

# Removing prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

num = 3 ^ 2  # '^' is a logical 'or' operator. Will come back to this in the future

# num = 3 ** 2
print(num)
