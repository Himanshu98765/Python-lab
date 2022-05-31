'''
lst=[]
x=int(input("ROW"))
y=int(input("COL"))
for i in range (x):
    tpl=()
    for j in range (y):
        n=int(input())
        tpl+=n,
    lst.append(tpl)
print(lst)
lst1,c=[],0
a=int(input("enter the no. you want to replaced"))
for i in range (x):
    tpl1=()
    for j in range (y-1):
        n=tpl[c]
        tpl1+=n,
        c+=1
    tpl+=a,
    lst.append(tpl)
print(lst)
'''
#Replpace last element of tuple of a list with a specific no.
lst=[]
x=int(input("ROW"))
y=int(input("COL"))
for i in range (x):
    tpl=()
    for j in range (y):
        n=int(input())
        tpl+=n,
    lst.append(tpl)
print(lst)
lst1=[]
a=int(input("enter the no. you want to replaced"))
for i in lst:
     z=i[:-1]+(a,)
     lst1.append(z)
print(lst1)
