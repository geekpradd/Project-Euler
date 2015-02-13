from functools import reduce
import itertools
 
def checkSet(param):
	for elem in param:
		org=set(list(param))
		org.remove(elem)
		if sum(org)<=elem:
			return False
	return True
def checkPythagoras(param):
	hypo=max(param)
	org=set(list(param))
	org.remove(hypo)
	sum=reduce(lambda a,b:a**2+b**2,org)
	if not hypo**2==sum:
		return False
	return True

def valuesforp(p):
	myset=[]
	for a in range(1,p+1):
		for b in range(1,(p-a)+1):
			c=p-a-b
			myset.append([a,b,c])
	output=list(filter(checkPythagoras,list(filter(checkSet, myset))))
	for li in output:
		output[output.index(li)]=frozenset(li)
	final=list(set(output))
	for li in final:
		final[final.index(li)]=set(li)
	return len(final)
def main():
	li=[]
	print("a")
	for num in range(1,1001):
		print("Currently at {0}".format(num))
		li.append(valuesforp(num))
	print("Answer is {0}".format(li.index(max(li))+1))
main()
#Answer is 840!! Yes!!