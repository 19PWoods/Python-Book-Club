# # The modulo operator (tells you the remainder)
# print(4 % 3)
# print(5 % 3)
# print(6 % 3)
# print(7 % 3)

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
# Note: every integer is divisible by 1.


# # Phil's Code
# # top of your program
# import timeit
# import numpy
# # user input
# start_time = timeit.default_timer()
# # number crunching and such
# prime_numbers = [2, 3, 5, 7]
# num = 10
# division = list(range(2, 11))
# while len(prime_numbers) < 1000:
#     remainders = []
#     for value in division:
#         remainders.append(num % value)
#     if numpy.prod(remainders) != 0:
#         prime_numbers.append(num)
#     num += 1
# print(prime_numbers)
# # print results and end of program
# stop_time = timeit.default_timer()
# print('Runtime (seconds): ', stop_time - start_time)
# print('\nLength of prime_numbers"', len(prime_numbers))
# top of your program

# import timeit
# import math
# import numpy
# # user input
# start_time = timeit.default_timer()
# # number crunching and such
# prime_numbers = []
# num = 2
# while len(prime_numbers) < 100:
#     remainders = []
#     division = int(round(math.sqrt(num)))
#     d = [1, division]
#     for value in d:
#         remainders.append(num % value)
#     if numpy.prod(remainders) != 0:
#         prime_numbers.append(num)
#     num += 1
# print(prime_numbers)
# # print results and end of program
# stop_time = timeit.default_timer()
# print('Runtime (seconds): ', stop_time - start_time)
# print('\nLength of prime_numbers"', len(prime_numbers))

# # Mari's Code
# # A Program to list the first X Prime numbers
# import math
# import timeit

# start_time = timeit.default_timer()

# x = 0
# number = 3
# primes = [2]
# extent = 100000  # modify to switch the number of primes reported
# while len(primes) < extent:
#     x = 0
#     if number % 2 == 0:
#         number = number+1
#     else:
#         for num in primes:
#             if num > math.sqrt(number):  # only have to check the square root of values
#                 break
#             elif number % num == 0:
#                 number = number+1
#                 x = 1
#                 break
#         if x != 1:
#             primes.append(number)
#             number = number+1
# # print(f"\nThe first {extent} prime numbers are:\n")
# print(primes)
# stop_time = timeit.default_timer()
# print('Runtime (seconds): ', stop_time - start_time)

# print(primes[-1])

# # Bob's Code
# # Find all prime numbers from 2 to max...

# # Imports...

# import timeit


# print("Howdy! This program will identify all prime\nnumbers from 1 to a user-defined maximum.\n")

# max_dividend = int(
#     input("   Enter the maximum (an integer) of the search range: "))


# primes = [2]

# current_dividend = 3

# start = timeit.default_timer()


# while (current_dividend <= max_dividend):

#     # print(f"Checking {current_dividend}")

#     current_divisor = 3

#     is_prime_flag = True

#     while ((current_divisor <= (int(current_dividend/2))) and (is_prime_flag == True)):

#         # print(f"Checking divisor = {current_divisor}")

#         if (current_dividend % current_divisor == 0):

#             is_prime_flag = False

#             break

#         current_divisor += 2

#     # Well, was it prime?

#     if (is_prime_flag == True):

#         # print("Yep!")

#         primes.append(current_dividend)

#     # else:

#         # print("Nope!")

#     current_dividend += 2


# # Print the prime numbers...

# number_of_primes = len(primes)

# print(
#     f"\nThere are {number_of_primes} prime numbers between 1 and {max_dividend}:")

# print(primes)


# # We're done...

# stop = timeit.default_timer()

# print('\nRuntime (in seconds): ', stop - start)

# print("\n\n")


# Find all prime numbers from 2 to max...
# divide by numbers up to the square root of the number being checked (thanks Mari!)
# 100000th prime was 1299709

# Imports...
import timeit
import math

print("Howdy! This program will identify all prime\nnumbers from 1 to a user-defined maximum.\n")
max_dividend = int(input("   Enter the maximum (an integer) of the search range: "))

primes = [2]
current_dividend = 3
start = timeit.default_timer()

while(current_dividend <= max_dividend):
print(f"Checking {current_dividend}")
current_divisor = 3
is_prime_flag = True
while((current_divisor <= (int(math.sqrt(current_dividend)))) and (is_prime_flag == True)):
#print(f"Checking divisor = {current_divisor}")
if(current_dividend % current_divisor == 0):
is_prime_flag = False
break
current_divisor += 2

# Well, was it prime?
if(is_prime_flag == True):
#print("Yep!")
primes.append(current_dividend)
#else:
#print("Nope!")

current_dividend += 2



# Print the prime numbers...
number_of_primes = len(primes)
print(f"\nThere are {number_of_primes} prime numbers between 1 and {max_dividend}.")
print(f"\nThe highest value prime found: {primes[-1]}")

# We're done...
stop = timeit.default_timer()
print('\nRuntime (in seconds): ', stop - start)
print("\n\n") 