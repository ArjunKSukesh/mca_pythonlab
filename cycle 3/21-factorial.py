a=int(input('Enter a number :'))
def fact(a):
    n=a
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact
print('factorial of',a,'is',fact(a))