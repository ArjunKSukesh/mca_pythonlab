x=int(input('Enter 1st number :'))
y=int(input('Enter 2nd number :'))
for i in range(1,min(x,y)+1):
 if(x%i==0 and y%i==0):
  gcd=i
print('gcd =',gcd)
