from math_functions import sum_till, sum_of_squares_till
"""Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""

def main(n):
    """ Finds the difference between the sum of the squares and the square of the
    sums of natural number from 1 to n."""

    return  (sum_till(n) ** 2) - sum_of_squares_till(n)

if __name__ == '__main__':
    print(main(100))



