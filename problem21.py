__author__ = 'Pradipta'

def factors(n):
    return [x for x in range(1,n) if not n%x]
def d(num):
    return sum(factors(num))

def amicable(number):

    if d(d(number))==number:
        return True

def main():
    output=[]
    for a in range(1,10000):
        if amicable(a):
            print(str(a) + " is an amicable number")
            output.append(a)
            output.append(d(a))
    total=sum(set(output))
    print (set(output))
    print("Sum is {0}".format(total))

main()