__author__ = 'Pradipta'
import math
isperfect = lambda x:int(math.sqrt(x)) == math.sqrt(x)
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
def oddcompos(n):
    return [x for x in list(set(range(2,n+1))-set(primes(n))) if x%2]
def main():
    a= oddcompos(10000)
    for b in [27]:
        r=int(primes(b)[-1])
        d=int((b-r))
        print(d, r , sep=' ')
        if isperfect(d):
            print('Oh yes it is')
main()