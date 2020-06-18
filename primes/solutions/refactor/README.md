1.  Let's look at refactoring each of the functions we wrote.

2.  First, is_prime:

    1.  The conditional statements at the beginning of the function can be 
        collapsed into a single check

            if num < 2:
    
    2.  QUESTION: Any way to improve the prime check??

    3.  Yes, we only need to check up to the floor(sqrt(num))

            for i in range(2, math.floor(math.sqrt(num) + 1)):
    
    4.  Run pytest to make sure that tests still pass

            pytest

3. Second, sum_of_primes:

    1.  Check for length is redundant due to iteration. Eliminate it.

    2.  Can use built-in sum() function and generator expression to condense code
        into a single line

            return sum(x for x in seq if is_prime(x))
    
    3.  Run pytest to make sure that tests still pass

            pytest