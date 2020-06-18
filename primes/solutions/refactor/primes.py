import math

def is_prime(num):
    """Determines whether a number is prime.

    Args:
        num: An integer value to check for primeness.
    
    Returns:
        True if the number is prime, else False.
    """
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
    """Calculates the sum of prime numbers in a sequence.

    Args:
        seq: The sequence containing numbers to evaluate for primeness and sum
    
    Returns:
        The sum of all prime integers in the sequence. If the sequence is empty
        or contains no primes, the return value will be 0.
    """
    return sum(n for n in seq if is_prime(n))
