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

# top of your program
import timeit
import numpy
# user input
start_time = timeit.default_timer()
# number crunching and such
prime_numbers = [2, 3, 5, 7]
num = 10
division = list(range(2, 11))
while len(prime_numbers) < 100:
    remainders = []
    for value in division:
        remainders.append(num % value)
    if numpy.prod(remainders) != 0:
        prime_numbers.append(num)
    num += 1
print(prime_numbers)
# print results and end of program
stop_time = timeit.default_timer()
print('Runtime (seconds): ', stop_time - start_time)
print('\nLength of prime_numbers"', len(prime_numbers))

# #A Program to list the first X Prime numbers
# import math
# import timeit

# start_time = timeit.default_timer()

# x=0
# number=3
# primes = [2]
# extent = 100000 #modify to switch the number of primes reported
# while len(primes)<extent:
#     x=0
#     if number%2 ==0:
#         number=number+1
#     else:
#         for num in primes:
#             if num > math.sqrt(number):
#                 break
#             elif number%num==0:
#                 number=number+1
#                 x=1
#                 break
#         if x!= 1:
#             primes.append(number)
#             number=number+1
# #print(f"\nThe first {extent} prime numbers are:\n")
# print(primes)
