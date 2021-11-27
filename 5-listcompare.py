list1=[]
list2=[]

a=int(input("Enter the number limit of list 1 :"))
for i in range(0,a):
 b=int(input("Enter the numbers :"))
 list1.append(b)
print(list1)

c=int(input("Enter the number limit of list 2 :"))
for j in range(0,c):
 d=int(input("Enter the numbers :"))
 list2.append(d)
print(list2)

list1_len=len(list1)
print("Lenght of the list 1 :",list1_len)

list2_len=len(list2)
print("Lenght of the list 2:",list2_len)

if list1_len==list2_len:
  print("Lenght of two list are same")
else:
  print("Lenght of two list are not same")

print("Sum of list 1 =",sum(list1))
print("Sum of list 2 =",sum(list2))

if sum(list1)==sum(list2):
  print("Sum of two list are same")
else:
  print("Sum of two list are not same")
for i in list1:
 for j in list2:
   if i==j:
     print("Element is found in both",i)


