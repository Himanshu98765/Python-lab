x=input("ENTER : ")
l=len(x)-1
res=""
for i in range(l):
	if i%2==0:
		res=res+x[i]
print(res)
