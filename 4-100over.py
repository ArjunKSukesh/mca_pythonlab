x=list(map(int,input('Enter some numbers :').split(' ')))
for i in range(0,len(x)):
 if x[i]>100:
  x[i]='over'
print(x)
