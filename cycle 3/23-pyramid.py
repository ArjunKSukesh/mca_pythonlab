def pyramid(num):
    for i in range(1,num+1):
        print()
        print(i,end="")
        j=1
        while j<i:
            print("",(i*(j+1)),end="")
            j=j+1
a=int(input("Enter N: "))
pyramid(a)