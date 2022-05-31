#find sum of all elements without using any function
tpl,sum=(),0
x=int(input("ROW"))
y=int(input("COL"))
for i in range (x):
    tpl1=()
    for j in range (y):
        n=int(input())
        tpl1+=n,
        sum+=n
    tpl+=tpl1,
print(tpl,"\nsum = ",sum)
