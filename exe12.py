from itertools import chain, combinations
from math_functions import factorise

"""What is the value of the first triangle number to have over five hundred divisors?"""

# Def triangular number
# The sequence of all triangular numbers is given
# by a_N = (N)(N+1)/2

def convert_to_list(d):
    """ (dict from math_functions.factorise) -> list
    Returns the expanded version of the factorise dict equivalent
    """

    result = []
    for k, v in d.items():
        result.extend([k]*v)
    return result

def all_combinations(t):
        """ list -> list
        Returns all the combinations of a given iterable t
        """

        # chain -> returns a flattened seuqence of originally
        # nested iterables
        # map -> applies a function (in this cae combination lambda function)
        # to every item in iterable
        
        return chain(*map(lambda x: combinations(t, x), range(0, len(t) + 1)))

def main():
    """ Solves Project Euler problem 12 """
    i = 3
    triangular_num = 6
    prime_factors = convert_to_list(factorise(triangular_num))
    all_factors = set(all_combinations(prime_factors))

    while len(all_factors) < 500:
        i += 1;
        triangular_num = i * (i + 1) // 2
        prime_factors = convert_to_list(factorise(triangular_num))
        all_factors = set(all_combinations(prime_factors))

    return triangular_num

if __name__ == "__main__":
    print(main())

