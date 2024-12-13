#!/usr/bin/python3
""" prime game module """


def is_prime(n):
    """Determine if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def count_primes_up_to_n(n, primes):
    """Count the number of primes up to n."""
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    Maria starts first. Both play optimally.
    """
    if not nums or x < 1:
        return None

    # Precompute primes up to the maximum number in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to_n(n, primes)
        # If the number of primes is odd, Maria wins (she starts)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
