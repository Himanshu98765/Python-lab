x=int(input("ENTER THE FIRST NO."))
y=int(input("ENTER THE SECOND NO."))
z=int(input("ENTER THE THIRD NO."))
if(x>y):
	if(x>z):
		print("GREATEST NO. AMONG 3 ARE : ",x)
	if(x<z):
		print("GREATEST NO. AMONG 3 ARE : ",z)
elif(x<y):
	if(y>z):
		print("GREATEST NO. AMONG 3 ARE : ",y)
	if(y<z):
		print("GREATEST NO. AMONG 3 ARE : ",z)
