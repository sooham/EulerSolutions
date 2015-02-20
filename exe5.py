"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import math_functions

def main():
    """ Solves problem 5 in project Euler"""
    print(math_functions.lcm(list(range(2,21))))

if __name__ == '__main__':
    main()


