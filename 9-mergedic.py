dic1={}
dic2={}
n=int(input("Enter the limit of 1st :"))
for i in range(n):
 key1=input("Enter the key :")
 value1=input("Enter the value :")
 dic1[key1]=value1
m=int(input("Enter the limit of 2nd :"))
for i in range(m):
 key2=input("Enter the key :")
 value2=input("Enter the value :")
 dic2[key2]=value2
print("1st dic :",dic1)
print("2nd dic :",dic2)
dic1.update(dic2)
print(dic1)
