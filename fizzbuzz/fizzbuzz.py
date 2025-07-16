#!/usr/bin/env python3
"""
FizzBuzz Implementation

This script implements the classic FizzBuzz problem:
- Prints "Fizz" for numbers divisible by 3.
- Prints "Buzz" for numbers divisible by 5.
- Prints "FizzBuzz" for numbers divisible by both 3 and 5.
- Prints the number itself if none of the above conditions are met.

The script iterates through numbers 1 to 50 and prints each result on a separate line.
Compatible with Python 3.10+.
"""


def fizzbuzz():
    """
    Prints the FizzBuzz sequence from 1 to 50.

    For each number in the range:
        - Prints "FizzBuzz" if the number is divisible by both 3 and 5.
        - Prints "Fizz" if the number is divisible by 3.
        - Prints "Buzz" if the number is divisible by 5.
        - Otherwise, prints the number itself.

    Returns:
        None
    """
    for number in range(1, 51):
        # Check divisibility by both 3 and 5 first to ensure correct output
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


if __name__ == "__main__":
    fizzbuzz()
