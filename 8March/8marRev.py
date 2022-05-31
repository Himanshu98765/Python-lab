a=int(input("ENTER THE  NUMBER : "))
rev=0
while (a!=0):
	t=a%10
	rev=(rev*10)+t
	a//=10
print(rev)
