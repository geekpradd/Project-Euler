__author__ = 'Pradipta'
def fibo():
    s=list()
    a,b=1,2
    while len(str(a))!=1000:
        print ('a is currently: {0}'.format(a))
        s.append(a)
        s.append(b)
        a=a+b
        b=b+a
    return len(s)+2

print('Answer is {0}'.format(fibo()))