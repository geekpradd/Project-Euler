is_whole = lambda a: str(a)[-1] == "0"

def product(sequence):
	if not len(sequence):
		return 1
	return sequence[0]*product(sequence[1::])

def pairs(n):
	a = []
	o = []
	try:
		for b in range(1,n+1):
			if not n%b and not b in a :
				a.append(b)
				a.append(n//b)
				o.append((b,n//b))
	except:
		pass
	return o
def gen_triples(n):
	for r in range(1,n+1):
		if is_whole(r*r/2):
			factors = pairs(r*r//2)
			if len(factors):
				for a in factors:
					yield((r+a[0],r+a[1],r+a[0]+a[1]))

for p in gen_triples(200):
	if sum(p) == 1000:
		print (product(p))

#Answer is 31875000

