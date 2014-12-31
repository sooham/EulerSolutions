'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

from math_functions import factorise

def main():
    ''' ()-> int
    Returns the answer to the project euler question.
    '''
    factors = factorise(600851475143)
    return max(factors)

print(main())