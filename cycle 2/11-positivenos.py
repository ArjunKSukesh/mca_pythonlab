a=list(map(int,input('Enter some numbers :').split( )))
b=[x for x in a if x!=0 and x>0]
print('list of positive numbers :',b)