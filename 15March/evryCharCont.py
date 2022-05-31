x=input("enter the string : ")
s,d,c=0,0,0
l=len(x)
for i in range(l):
	if(ord(x[i])>=48 and ord(x[i])<=57):	d+=1
	elif((ord(x[i])>=65 and ord(x[i])<=90) or (ord(x[i])>=97 and ord(x[i])<=122)):	s+=1
	else:	c+=1
print("there are ",d," digits in the string")
print("there are ",s," alphabets in the string")
print("there are ",c," special characters in the string")
