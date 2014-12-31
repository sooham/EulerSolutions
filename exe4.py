"""A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math_functions import is_palindrome
def main():
    """ ()-> int
    Returns the answer to the project euler problem.
    """
    result = 0 
    for i in range(100, 1000):
        for j in range(100, 1000):
            mult = i * j
            if is_palindrome(mult) and mult > result:
                result = mult

    return result

print(main())