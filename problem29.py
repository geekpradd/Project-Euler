def getUnique():
  d=[]
  for a in range(2,101):
    for b in range(2,101):
      d.append(a**b)
  print (len(set(d)))

getUnique()
