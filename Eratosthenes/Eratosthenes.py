def eratosthenes(n):
# This function returns a list of prime numbers up to n using the Sieve of Eratosthenes algorithm.
# The algorithm works by marking the multiples of each prime number starting from 2 as non-prime.
# The remaining numbers are prime.
    primeNumber = 2
    primeNumbers = [True] * (n+1)
    while primeNumber * primeNumber < n:
        if primeNumbers[primeNumber]:
            for i in range(primeNumber*primeNumber, n+1, primeNumber):
                primeNumbers[i] = False
        primeNumber += 1
# the reason using primeNumber * primeNumber is when we reach a prime number p, all multiples of p less than p^2 have already been marked as non-prime
    return [i for i in range(2, n+1) if primeNumbers[i]]
        
# Example usage:
n = int(input("Enter the number to find prime numbers up to it: "))
print(f"Prime numbers up to {n}: {eratosthenes(n)}")
