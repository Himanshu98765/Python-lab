n=int(input("ENTER THE NUMBER you want fabonacii series (more than 2) : "))
a,b=0,1
print(a,",",b,end="")
for i in range(n-2):
	a,b=b,a+b
	print(",",t,end="")
print("\n")
