def fib(num):
    f=0
    s=i=1
    print("Fibonacci Series:",f,end="")
    while i<num:
        print("",s,end="")
        t=f+s
        f=s
        s=t
        i=i+1
a=int(input("Enter Limit: "))
fib(a)
