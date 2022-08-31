#!/usr/bin/env python3

import math
import cmath
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# This program calculates the subprime fibs of Conway

a = 62  # first number of the sequence
b = 37  # second number of the sequence.
s = 0  # initialize the sum

# Let's check the results for N numbers in the sequence.
N = 1000
sequence = [0] * N
sequence[0] = a
sequence[1] = b


# print(sequence)
# The sequence is defined by taking n and n1 and adding them together (n + n1 =s). If the result is a prime number we append it to the list without modification.
# If the number is not a prime then we then we divide it by its smallest prime divisor and then append that to the list and add the last 2 numbers we have.
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


def sum(counter):
    s1 = sequence[counter - 2] + sequence[counter - 1]
    return s1


def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sequence_function():
    counter = 2

    while (counter < N):
        s = sum(counter)
        l = is_prime(s)
        if l:
            sequence[counter] = s
            counter += 1
        else:
            nnum = smallestDivisor(s)

            next = s / nnum
            sequence[counter] = next
            counter += 1
    return sequence


# def smallest_prime_divisor(p):
#     DivisorRange = range(2, p )
#
#     list = [i for i in DivisorRange if p % i == 0]
#     return list[0]

def smallestDivisor(n):
    if (n % 2 == 0):
        return 2;

    for i in range(3, int(np.sqrt(n)) + 1, 2):

        if n % i == 0:
            return i;


maximum = np.max(sequence_function())
new_list = sequence_function()

ma = int(maximum)
print(ma)
# freq = np.zeros(ma+1)
freq = []
x = []
for i in range(1, ma + 1):
    counting = countX(new_list, i)
    if counting == 0:
        continue
    else:
        freq.append(counting)
        x.append(i)

# print(freq,x)
print(sequence_function())

# print(sequence_function())
# bin_values = np.arange(start=1, stop=ma, step=20)
# print(max(sequence_function()))
# plt.hist(freq,bins=bin_values)
plt.figure(figsize=(15, 15))
plt.plot(sequence_function())
plt.grid()
plt.show()