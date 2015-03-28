def getmiddle(string):
    if len(string)%2:
        return string[int((len(string)-1)/2):-int(((len(string)-1)/2))]
    else:
        return None

def ispalindrome(n):
    string=str(n)
    if not len(string)%2:
        a=int(len(string)/2)
        firstpart, secondpart = string[:a], string[a:]

        if firstpart==secondpart[::-1]:
            return True
        return False
    else:

        string=string.replace(getmiddle(string),'')
        a=int(len(string)/2)
        firstpart, secondpart = string[:a], string[a:]
        if firstpart==secondpart[::-1]:
            return True
        return False

def return_list():
    ret = set()
    for a in range(100,1000):
        for b in range(100,1000):
            ret.add(a*b)
    return ret

def main():
    x = filter(lambda a: ispalindrome(str(a)),return_list())
    print (max(x))

main()

#Answer is 906609