dict={}
n=int(input("Enter the limit :"))
for i in range(n):
 key=input("Enter the key :")
 value=input("Enter the value :")
 dict[key]=value
print(dict)
keys_sorted=sorted(dict.keys())
for i in keys_sorted:
	print(i,',',dict[i])
print("descending order:")
for i in sorted(dict.keys(),reverse=True):
	print(i,',',dict[i])
