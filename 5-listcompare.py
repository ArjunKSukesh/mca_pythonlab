count=0
a=list(map(int,input("enter 1st list of numbers seperated by comas : ").split(' ')));
b=list(map(int,input("enter 2nd list of numbers seperated by comas : ").split(' ')));
if len(a)==len(b):
    print("both list is of same length....")
else:
    print("both list are of different length.....")


if sum(a)==sum(b):
    print("sum of both list is equal....")
else:
    print("sum of both list is not equal....")

for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            print(a[i]," occure in both")
            count+=1
if count==0:
    print("no values occure in both lists")


