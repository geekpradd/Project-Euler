__author__ = 'Pradipta'
def primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
def is_prime(num):
    if len(factors(num))==1:
        return True
    return False
def factors(n):
    return [x for x in range(1,n) if not n%x]

print(primes(2000000))