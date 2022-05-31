a=n=int(input("ENTER THE  NUMBER : "))
rev=0
while (a!=0):
	t=a%10
	rev=(t**3)+rev
	a//=10
if (rev==n):
	print(n," is a armstrong no. ")
else:
	print(n," is not a armstrong no. ")
