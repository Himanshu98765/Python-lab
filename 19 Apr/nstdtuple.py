#nested tuple
tpl,tpl2=(),()
n=int(input("ENTER THE NO. OF ELEMENTS : "))
for i in range(n):
    y=input("ENTER : ")
    tpl+=y,

y=int(input("COL : "))
x=(n//y)
c=0
for i in range (x):
    tpl1=()
    for j in range (y):
        p=tpl[c]
        tpl1+=p,
        c+=1
    tpl2+=tpl1,
if(n%2==1):
     tpl2+=tpl[n-1],
print(tpl)
print(tpl2)
