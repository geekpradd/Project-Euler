def factorial(n):
	exceptions=[0,1]
	if n in exceptions:
		return 1
	else:
		return n*factorial(n-1)
combination=lambda a,b:factorial(a)/factorial(b)/factorial(a-b)
def comboloop(num):
	li=[]
	n=0
	while n<=num:
		li.append(int(combination(num,n)))
		n+=1
	return li
def main():
	num=1
	holder=[]
	while num<=100:
		holder.append(tuple(comboloop(num)))
		num+=1
	numberofvalues=0
	for tup in holder:
		for value in tup:
			if value>1000000:
				numberofvalues+=1
	
	print(numberofvalues)
main()
#The answer is 4075! Hiphip Hurray!