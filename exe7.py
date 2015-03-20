"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13. What is the 10 001st prime number?"""

from math_functions import find_nth_prime

def main(n):
    """ Returns the n-th prime number in the range of all nutural numbers"""
    return find_nth_prime(n)

print(main(10001))
