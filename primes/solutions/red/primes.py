def is_prime(num):
    if num < 0:
        return False
    elif num == 0:
        return False
    elif num == 1:
        return False
    else:
        # Iterate over values between 2 and num. If num mod val == 0, then
        # num can't be prime
        for i in range(2, num):
            if num % i == 0:
                return False

        # If we get here, 1 and num are the only factors!
        return True

def sum_of_primes(seq):
    if len(seq) == 0:
        return 0

    sum = 0
    for val in seq:
        if is_prime(val):
            sum += val
    
    return sum
