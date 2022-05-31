#joint elements of tuple and make string
n=int(input("ENTER THE NO. OF ELEMENTS : "))
tpl=()
x=""
for i  in range (n):
     y=input("enter: ")
     tpl+=y,
for i in range(n):
     x+=tpl[i]
print(tpl,"\n",x)
