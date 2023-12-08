"""
Module to hold library functions.
"""


def power(n):
    """
    Function to generate a function that raises a number to a power.
    """

    def closure(num):
        return num**n

    return closure
