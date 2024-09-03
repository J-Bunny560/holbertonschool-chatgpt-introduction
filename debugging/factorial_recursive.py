#!/usr/bin/python3
import sys

# Function Description
# -------------------
# The factorial function calculates the factorial of a given integer.
# It uses a recursive approach to compute the result.

def factorial(n):
    # Parameters
    # ----------
    # n (int): The input number for which the factorial is calculated.

    # Returns
    # -------
    # int: The factorial of the input number.

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the factorial of the command-line argument and print the result
f = factorial(int(sys.argv[1]))
print(f)