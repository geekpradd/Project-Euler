__author__ = 'Pradipta'
l=lambda x:len(x)%2
def getmiddle(string):
    if l(string):
        return string[int((len(string)-1)/2):-int(((len(string)-1)/2))]
    else:
        return None

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
def main():
    out=[]
    for n in range(1,1000001):
        if ispalindrome(n) and ispalindrome(bin(n)[2::]):
            print("{0} is double palindrome".format(n))
            out.append(n)
    print('Answer is {0}'.format(sum(out)))
print(ispalindrome(1111111110000111101))