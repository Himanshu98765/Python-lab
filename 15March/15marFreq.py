x=input("enter the string : ")
a=input("ENTER THE CHARACTER YOU WANT TO SEARCH : ")
c=0
l=len(x)
for i in range(l):
	if(x[i]==a):
		c+=1
print("THE FREQUENCY OF ",a," IS ",c)
