a=input('Enter a line of text :').split(' ')
print(a)
for i in set(a):
    count=1
    for k in range(a.index(i)+1,len(a)):
        if i==a[k]:
            count+=1
    print(i,'occurs',count,'times')
    