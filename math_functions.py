import math

fib_values = {1:1, 2:2}

def is_palindrome(num):
    """ (int) -> bool
    Return True iff the number is palindromic.
    """
    return str(num) == str(num)[::-1]

def fib(n):
    ''' (int) -> int
    Computes the Fibonacci sequence to the n-th term where the first term is
    1 and the 2nd term is 2.
    '''
    global fib_values

    if n in fib_values:
        return fib_values[n]
    else:
        # compute the term using recursion and add the key-value pair
        # to fib values
        ans = fib(n-1) + fib(n-2)
        fib_values[n] = ans
        return ans

def soe(n):
    """ (int) -> prime generator
    Returns the generator of all prime numbers upto n inclusively using the
    Sieve of Eratosthenes algorithm.
    """
    # intially, I tried to implement this algorithm using the normal looping
    # constructs, however, I am currently appempting to implement the functions
    # using the generator and yield constructs
    A = [True] * (n + 1)
    A[0] = A[1] = False

    # a number i is considered to be prime iff the value of A[i] is True
    # and the soe() function has terminated.
    # We consider all numbers x to be prime iff A[x] is True
    for i, is_prime in enumerate(A):
        # check if the number i is prime
        if is_prime:
            yield i
            # then eliminate all the muliples of this prime greater than itself
            for j in range(2, (n // i + 1)):
                A[(i * j)] = False



def factorise(n, res= None):
    ''' (int) -> dict
    Returns the dict of tuple of format where the first int is
    the prime factor of the number n and the second int is the number of times
    the prime factor occurs.
    '''

    if n <= 1:
        return {}

    # we can put an upper limit to the number of numbers we need to check for
    # factorisation with, as the quotient of the number will also be evaluated
    # for its prime factors. This reduces the number of steps in the algorihtm
    upper_limit = math.sqrt(n)
    found_divisor = False
    i = 2
    if res == None:
        result = {}
    else:
        result = res

    while i <= upper_limit and not found_divisor:
        # find the very first divisor of the number
        # by mathematical proof the very first divisor is always prime
        # if there are no divisors found in the while loop then the number
        # is prime
        quo, rem = divmod(n, i)
        if rem == 0: # then we have found a divisor
            # find the divisors of the quotient
            factorise(quo, result)
            result[i] = result.get(i, 0) + 1
            found_divisor = True
        i += 1

    # if the value of found_divisor is still False then the number n is prime
    if not found_divisor:
        result[n] = result.get(n, 0) + 1

    return result

def product(factors):
    """ (dict from factorise) -> int
    Returns the total of the dictionary of factors
    """
    return sum([prime * n for prime,n in factors.items()])

def lcm(lst):
    """ (list of int) -> int
    Returns the lcm of all numbers in lst.
    """
    final_list = lst[:]
    while any([final_list[0] != x for x in final_list[1:]]):
        max_final_list = max(final_list)
        for i in range(len(final_list)):
            while final_list[i] < max_final_list:
                final_list[i] += lst[i]
            print(final_list)
    return final_list[0]

def sum_of_squares_till(n):
    """ (int) -> int
    Returns the sum of the squares of the all numbers from 1 to n.
    Precondition: n >= 1
    """
    # find the result using the sum of squares telescoping series
    return int(n * (n + 1) * (2 * n + 1) / 6)

def sum_till(n):
    """ (int) -> int
    Return the sum of all numbers from 1 to n.
    Precondition: n >= 1
    """
    # find the result using the geometric series.
    return int((n + 1) * n / 2)

def find_nth_prime(n):
    """ (int) -> int
    Returns the n-th prime number
    """
    # The n-th prime is approximately located around the number m
    # when n * ln(n) + n*ln(ln(n)) forall n <= 6
    upper_bound = math.ceil(n * math.log(n) + n * math.log(math.log(n)))
    # use seive on the range [1, upper_bound]
    primes_found = 0
    for prime in soe(upper_bound):
        primes_found += 1
        if primes_found == n:
            return prime

