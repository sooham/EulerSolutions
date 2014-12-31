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
