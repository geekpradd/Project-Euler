def sumofdigits(number):
	return sum([int(x) for x in str(number)])

def main():
	a,b=1,1
	dic=[]
	while a<100:
		
		while b<100:
			
			dic.append(sumofdigits(a**b))
			
			b+=1
		
		a+=1
		b=0
	print(max(dic))
main()
