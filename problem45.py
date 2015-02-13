__author__ = 'Pradipta'
def triangular(n):
    out=list()
    while len(out)!=n:
        a=len(out)+1
        out.append(a*(a+1)/2)
    return out
def pentagonal(n):
    out=list()
    while len(out)!=n:
        a=len(out)+1
        out.append(a*(3*a-1)/2)

    return out
def hexagonal(n):
    out=list()
    while len(out)!=n:
        a=len(out)+1
        out.append(a*(2*a-1))
    return out

def main():
    a=set(triangular(100000))
    b=set(pentagonal(100000))
    c=set(hexagonal(100000))
    print("Answer is " + str(list(a.intersection(b,c))[-1]))
main()