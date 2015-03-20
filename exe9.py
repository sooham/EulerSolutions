"""A pythagorean triplet is a set of three natural number, a < b < c for which
a^2 + b^2 = c^2. There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc"""

def main():
    """ Returns the result to question 9"""
    # a + b + c = 1000
    # a^2 + b^2 = (1000 - a -b)^2
    # 0 = 1000000 - 2000(a + b) + 2ab
    # 2000a - 2ab = 1000000 - 2000b
    # 1000a -ab = 500000 - 1000b
    # a(1000 - b) = 500000 - 1000b
    # a = (500000 - 1000b) / (1000 - b)
    # search for ints

    for i in range(1, 500):
        a = (500000 - 1000 * i) / (1000 - i)
        if a % 1 == 0:
            # then a is int
            return int(a * i * (1000 - a - i))
    return -1

if __name__ == "__main__":
    print(main())
            
