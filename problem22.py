import requests

def main():
    print("Getting data")
    mapdata = {}
    for b, a in enumerate('abcdefghijklmnopqrstuvwxyz'):

        mapdata[a.upper()]=b+1
    lis=requests.get('https://projecteuler.net/project/resources/p022_names.txt').text.replace('"',' ').strip().split(',')
    mylist = sorted([x.strip(' ') for x in lis])
    print (mylist[:3:])

    score=0

    for index,data in enumerate(mylist):
        value=0
        for letter in data:
            value+=mapdata[letter]
        score+=value*(index+1)
        print("Score is now " + str(score))

main()
