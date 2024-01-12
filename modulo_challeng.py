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
# Note: every integer is divisible by 1, so this condition does not have to be tested

# top of your program
import timeit
import numpy as np
# user input
start_time = timeit.default_timer()
# number crunching and such
prime_numbers = []
num = 2
division = range(2, 11)
while range(prime_numbers) < 101:
    for value in range(division):
        remainders = num % value
        if np.prod(remainders) != 0:
            prime_numbers.append(num)
    num += 1
# print results and end of program
stop_time = timeit.default_timer()
print('Runtime (seconds): ', stop_time - start_time)


# # top of your program
# import timeit
# # user input
# start_time = timeit.default_timer()
# # number crunching and such
# prime_numbers = []
# num = 2
# while range(prime_numbers) > 101:
#     for value in range(division):
#         if num % value ==
# # print results and end of program
# stop_time = timeit.default_timer()
# print('Runtime (seconds): ', stop_time - start_time)
