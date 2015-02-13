def genchamp(digits):
	part=''
	for a in range(1,digits+1):
		part+=str(a)
		
	return part
def product(sequence):
	if len(sequence)==1:
		return sequence[0]
	else:
		return sequence[0]*product(sequence[1::])
def main():
	s=genchamp(1000000)
	
	a=[s[1-1],s[10-1],s[100-1],s[1000-1],s[10000-1],s[100000-1],s[1000000-1]]
	print(a)
	print(product([int(c) for c in a]))
main()
#The answer is 210! Yes!