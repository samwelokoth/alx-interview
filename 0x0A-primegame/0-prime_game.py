#!/usr/bin/python3

def sieve_of_eratosthenes(max_num):
    """ Returns a list of prime numbers up to max_num """
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    # Find all prime numbers up to the maximum n in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes less than or equal to n
        prime_count = sum(1 for prime in primes if prime <= n)

        # Determine the winner based on the count of primes
        if prime_count % 2 == 1:  # Odd number of primes
            maria_wins += 1
        else:  # Even number of primes
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # If there's a tie

# Example test case
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
