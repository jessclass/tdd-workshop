from primes import is_prime, sum_of_primes

def test_prime_negative():
    assert not is_prime(-124387921)
    assert not is_prime(-1000)
    assert not is_prime(-3)

def test_prime_zero():
    assert not is_prime(0)

def test_prime_one():
    assert not is_prime(1)

def test_prime_primes():
    assert is_prime(2)
    assert is_prime(89)
    assert is_prime(514229)

def test_prime_composites():
    assert not is_prime(4)
    assert not is_prime(100)
    assert not is_prime(514230)

def test_sum_of_primes_empty():
    assert sum_of_primes([]) == 0

def test_sum_of_primes_no_primes():
    assert sum_of_primes([4, 6, 8, 100]) == 0

def test_sum_of_primes_some_primes():
    assert sum_of_primes([2, 4, 5, 89, 100]) == 96

def test_sum_of_primes_all_primes():
    assert sum_of_primes([2, 5, 7, 89]) == 103