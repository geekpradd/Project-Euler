__author__ = 'Pradipta'
import itertools
flatten_iter = itertools.chain.from_iterable

def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
def factors(n):
    return set(flatten_iter((i, n//i)
                for i in range(1, int(n**0.5)+1) if n % i == 0))
def primes(n):
    return list(itertools.takewhile(lambda p: p<n, erat2()))
def main():
    no=600851475143
    facs=factors(no)
    s=[]
    for a in facs:
        if len(factors(a))==2:
            s.append(a)
    print(max(s))
main()