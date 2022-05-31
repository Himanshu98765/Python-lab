#tuple in  list
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
