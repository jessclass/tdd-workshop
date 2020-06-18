import math

def is_prime(num):
    if num < 2:
        return False
    else:
        # Iterate over values between 2 and num. If num mod val == 0, then
        # num can't be prime
        for i in range(2, math.floor(math.sqrt(num) + 1)):
            if num % i == 0:
                return False

        # If we get here, 1 and num are the only factors!
        return True

def sum_of_primes(seq):
    return sum(n for n in seq if is_prime(n))
