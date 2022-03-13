a=int(input("ENTER ANY NO. : "))
s=0
n=a*a
while(n!=0):
	t=n%10
	s+=t
	n//=10
if(s==a):	print("IT IS A NEON NO. ")
else:	print("IT IS NOT A NEON NO. ")
