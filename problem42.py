with open('problem42txt.txt','r') as f:
	data=f.read()
triangular=lambda x:1/2*x*(x+1)
mapping={}
for b,a in enumerate('abcdefghijklmnopqrstuvwxyz'):
	mapping[a]=b+1
def is_triangularword(word):
	sequence=[mapping[a] for a in word.lower()]
	return is_triangular(sum(sequence))
def is_triangular(num):
	for a in range(1,num+1):
		if triangular(a)==num:
			return True
		elif triangular(a)>num:
			return False
def gen(d):
	return[x.replace('"','') for x in d.split(',')]
def main():
	count=0
	for li in gen(data):
		if is_triangularword(li):
			count+=1
	print(count)
main()
#Answer is 162!! yeah!