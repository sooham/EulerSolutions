import math

fib_values = {1:1, 2:2}

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
    """ (int) -> list
    Returns the list of all prime numbers upto n inclusively using the
    Sieve of Eratosthenes algorithm.
    """

    candidates = list(range(2, n+1))
    primes = candidates[:] # hold the final version of candidates list

    for num_1 in candidates:
        found_first_mult = False
        if num_1 in primes:
            for num_2 in primes:
                # find and keep the first multiple of num_1
                # remove all others
                if num_2 % num_1 == 0:
                    if not found_first_mult:
                        found_first_mult = True
                    else:
                        primes.remove(num_2)
    return primes

def factorise(n, res= None):
    ''' (int) -> dict
    Returns the dict of tuple of format where the first int is
    the prime factor of the number n and the second int is the number of times
    the prime factor occurs.
    '''

    if n <= 1:
        return None

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