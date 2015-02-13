l=lambda x:len(x)%2
def getmiddle(string):
    if l(string):
        return string[int((len(string)-1)/2):-int(((len(string)-1)/2))]
    else:
        return None
def factors(n):
    return [x for x in range(1,n+1) if not n%x]
def ispalindrome(n):
    string=str(n)
    if not l(string):
        a=int(len(string)/2)
        firstpart, secondpart = string[:a], string[a:]

        if firstpart==secondpart[::-1]:
            return True
        return False
    else:

        string=string.replace(getmiddle(string),'')
        a=int(len(string)/2)
        firstpart, secondpart = string[:a], string[a:]
        print(firstpart,secondpart[::-1])
        if firstpart==secondpart[::-1]:
            return True
        return False
def getpairs(m):
    facs=factors(m)
    c=lambda x:len(str(x))==3
    x=[a for a in facs if c(a)]
    f=[]
    for elem in x:
        for d in x:
            if elem*d==m:
                f.append([elem,d])
    return f
def getpalindromes():
    s=[]
    for a in range(1,998002):
        print("At {0}".format(a))
        if ispalindrome(a):
            s.append(a)
    return s
def do(l):
    if len(getpairs(l))==2:
        return True
    return False

def main():
    l=getpalindromes()
    s=[]
    for a in l:
        if do(a):
            s.append(a)
    print(s)
main()
