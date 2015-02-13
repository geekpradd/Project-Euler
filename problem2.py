__author__ = 'Pradipta'
def fibo():
    s=[]

    a,b=1,2
    while a<4000001:

        s.append(a)
        s.append(b)
        a=a+b
        b=b+a
    return s
def main():
    total=sum([x for x in fibo() if not x%2])
    print(total)
main()