__author__ = 'Pradipta'
from functools import reduce

def check(n,c):
    l=[int(a)**c for a in list(str(n))]
    if n==sum(l):
        print("Voila")
check(1634)