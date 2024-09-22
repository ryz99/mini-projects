import math

test = input("who are you?")

print(f'hi {test}!')

print("yet another test")

def primes(n: int):
    sieve = [True] * n

    res = []

    for i in range (2, n):
        if sieve[i]:
            res.append(i)
            for j in range(i*i, n, i):
                sieve[j] = False

xs = primes(100)
ys = primes("the")


