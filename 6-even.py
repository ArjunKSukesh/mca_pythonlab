list1=[]
n=int(input("enter the limit :"))
for i in range(n):
 n1=int(input("enter a number :"))
 list1.append(n1)
print("Entered list :",list1)
odd=[]
for i in range(0,len(list1)):
 if list1[i]%2!=0:
  odd.append(list1[i])
print("odd numbers :",odd)
