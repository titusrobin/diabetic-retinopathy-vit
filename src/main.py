"""
Top level script.
"""
from lib.func_utils import power

if __name__ == "__main__":
    squarer = power(2)
    print(f"Square of 3 is {squarer(3)}.")

    cuber = power(3)
    print(f"Cube of 4 is {cuber(4)}.")

    inverter = power(-1)
    print(f"Inverse of 2 is {inverter(-2)}.")
