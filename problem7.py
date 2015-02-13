import itertools
flatten_iter = itertools.chain.from_iterable
def factors(n):
    return list(set(flatten_iter((i, n//i)
                for i in range(1, int(n**0.5)+1) if n % i == 0)))

def is_prime(n):
  if factors(n)==[1,n]:
    return True
  else:
    return False
def summation(numbers):
  x=0
  for a in numbers:
    print (a)
    x+=a
  return x
def getPrimes():
  li=[]
  for a in range(1,10000000000000000):
    if is_prime(a):
      li.append(a)
    if len(li)==10001:
      break
  return li
def main():
  primeNos= getPrimes()
  print (primeNos[10000])

main()
