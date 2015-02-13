__author__ = 'Pradipta'

is_even = lambda x: not x%2
def generate(n):
    loop=n
    output=list()
    while loop!=1:
        output.append(loop)
        if is_even(loop):
            loop=loop/2
        else:
            loop=3*loop+1
    output.append(1)
    output=[int(a) for a in output]
    return output
def main():
    calc={}
    d=[]
    for num in range(2,1000001):
        print("Currently at  {0}".format(num))
        calc[num]=len(generate(num))
        d.append(len(generate(num)))
    high=max(d)
    for val in calc.keys():
        if calc[val]==high:
            print("Answer is {0}".format(val))
            break

print(len(generate(837799)))

