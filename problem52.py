def calc(num):
	total=[num,num*2,num*3,num*4,num*5,num*6]
	li=[frozenset(str(a)) for a in total ]
	return len(set(li))==1
def main():
	num=1
	base=False
	while not base:
		base=calc(num)
		num+=1
	print("Answer is {0}".format(num-1))
main()
#Answer is 142857!.. i did it