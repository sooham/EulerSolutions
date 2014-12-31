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