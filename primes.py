"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2


    if number_of_primes <= 0:
        raise ValueError("number_of_primes cannot be less or equal to 0")

    while len(list)<number_of_primes:
        is_prime = True

        for j in range(2, num // 2 + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            list.append(num)
        num += 1


    return list
