def main():
  value=0
  for a in range(1,1001):
    value+=a**a
  print (str(value)[-10::])

main()
