a=int(input('Enter a number :'))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,'is not a prime number')
    else:
        print(a,'is a prime number')
else:
    print(a,'is not a prime number') 
