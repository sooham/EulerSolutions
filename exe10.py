'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''
import math
from math_functions import soe

def main():
    ''' ()-> int
    Returns the answer to the project Euler solution.
    '''

    primes = soe(2000000)
    result = 0
    for p in primes:
        result += p

    return result

print(main())
