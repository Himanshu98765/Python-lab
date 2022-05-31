a=n=int(input("ENTER THE  NUMBER : "))
rev=0
while (a!=0):
	t=a%10
	rev=(rev*10)+t
	a//=10
if (rev==n):
	print(n," is a palindrome no. ")
else:
	print(n," is not a palindrome no. ")
