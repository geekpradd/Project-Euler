__author__ = 'Pradipta'
def divides(num,sequence):
    for a in sequence:
        if num%a:
            return False
    return True
def product(sequence):
    if len(sequence)==1:
        return sequence[0]
    else:
        return sequence[0]*product(sequence[1::])
def lcm(sequence):
    for a in range(1,product(sequence)+1):
        print ("Currently at {0}".format(a))
        if divides(a,sequence):
            return a
print(lcm(range(1,20)))