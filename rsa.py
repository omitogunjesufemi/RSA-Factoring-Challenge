#!/usr/bin/python3
import math
import sys

def main(argv):
    """This is the entry point of the program"""
    with open(argv[1], "r") as test_file:
        rsa_number = test_file.read()
        get_prime_factors(rsa_number)

def get_prime_factors(number):
    n = int(number)
    x = 0
    y = 0
    for i in range(n + 100):
        x = math.sqrt(n + (i**2))
        if int(x) - x == 0:
            y = int(i)
            x = int(x)
            break
    p, q = (x + y, x - y)
    print("{}={}*{}".format(n, p, q))

if __name__ == "__main__":
    main(sys.argv)
