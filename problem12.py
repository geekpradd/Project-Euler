from functools import reduce 
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def triangular(n):
	for a in range(1,n+1):
		yield sum(range(1,a+1))

for a in triangular(1000000):
	print ("Current Number is {0}".format(a))
	if len(factors(a))>500:
		print (a)
		break 

#Answer was 76576500