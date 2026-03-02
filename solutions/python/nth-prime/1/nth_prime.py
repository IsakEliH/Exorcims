import math


def prime(number):

    if number < 1:
        raise ValueError("there is no zeroth prime")

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    lst_primes: list = []

    n = 0
    while len(lst_primes) < number:
        if is_prime(n):
            lst_primes.append(n)
            # yield lst_primes[-1]

        n += 1

    return lst_primes[-1]
