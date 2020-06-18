1.  Create the files primes.py and test\_primes.py

        touch primes.py test_primes.py

2.  Write tests for the is\_prime method. Look at the contract!

    1.  Negative, 0, and 1 are known to be not prime. Write a test for that.

            def test_prime_negative():
                assert not is_prime(-124387921)
                assert not is_prime(-1000)
                assert not is_prime(-3)

            def test_prime_zero():
                assert not is_prime(0)

            def test_prime_one():
                assert not is_prime(1)

    2.  More interesting tests are anything above 1. Write tests for that.

            def test_prime_primes():
                assert is_prime(2)
                assert is_prime(89)
                assert is_prime(514229)

            def test_prime_composites():
                assert not is_prime(4)
                assert not is_prime(100)
                assert not is_prime(514230)

3.  Run the tests, they will fail!

        pytest

4.  This is expected behavior. We have written our tests, but the functions 
    under test have not even been written yet!

5.  Let's start writing some actual code.

        def is_prime(num):
            if num < 0:
                return False
            elif num == 0:
                return False
            elif num == 1:
                return False
            else:
                return True

6.  This definitely won't work, but let's just prove to ourselves that some
    of our tests are actually good now.

        pytest

7.  We're still "red" because we haven't handled any of the interesting stuff!
    Let's fix that.

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

8.  That's all it should take to validate is\_prime. Is it the fastest code? No, but
    at least it's something.

        pytest

9.  This puts us into Green! Good job!

10. Now, let's do this for the sum_of_primes function.

11. First, let's write some tests for the sum_of_primes that will fail.

        def test_sum_of_primes_empty():
            assert sum_of_primes([]) == 0

        def test_sum_of_primes_no_primes():
            assert sum_of_primes([4, 6, 8, 100]) == 0

        def test_sum_of_primes_some_primes():
            assert sum_of_primes([2, 4, 5, 89, 100]) == 96

        def test_sum_of_primes_all_primes():
            assert sum_of_primes([2, 5, 7, 89]) == 103

12. Run tests to make sure that they fail

        pytest

13. Implement sum_of_primes so that tests will pass

        def sum_of_primes(seq):
            if len(seq) == 0:
                return 0

            sum = 0
            for val in seq:
                if is_prime(val):
                    sum += val
            
            return sum

14. Check that tests are passing

        pytest

15. Tests should all pass, and we're back to green!
