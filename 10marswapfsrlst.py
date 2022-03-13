a=n=int(input("ENTER ANY NO. : "))
i=1
t=1
while(n!=0):
	t=n%10
	if(i==1):	print(t,end="")
	n//=10
	i*=10
m=a-(t*(i))
m//=10
print(m,t)
