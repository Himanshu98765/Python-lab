n=int(input("ENTER THE 10 DIGIT MOBILE NO. : "))
i=1
a=0
b=0
while(n!=0):
	t=n%10
	if(i%2==1):	a+=t
	else:	b+=t
	n//=10
	i+=1
if(a==b):	print("IT IS A MAGIC NO.")
else:	print("IT IS NOT A MAGIC NO.")
