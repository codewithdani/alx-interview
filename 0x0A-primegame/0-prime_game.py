#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve_list = [True] * (n + 1)
    for prime_candidate in range(2, n + 1):
        if sieve_list[prime_candidate]:
            prime.append(prime_candidate)
            for i in range(prime_candidate, n + 1, prime_candidate):
                sieve_list[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
