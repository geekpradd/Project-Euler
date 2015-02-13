__author__ = 'Pradipta'
triangular=lambda x:int(x*(x+1)/2)
factors=lambda n:[a for a in range(1,n+1) if not n%a]
divisors,num=0,1
while divisors!=501:
    print("At {0}".format(num))
    n=triangular(num)
    divisors=len(factors(triangular(num)))
    num+=1
print("Answer is {0}".format(n))