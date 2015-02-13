
def factorial(n):
  if not n:
    return 1
  else:
    return n * factorial(n-1)

def main():
  no=str(factorial(100))
  num=0
  for x in list(no):
    num+=int(x)
  print (num)
main()
