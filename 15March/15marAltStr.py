x=input("enter the string : ")
i=0
l=len(x)
str=" "
while (i<l):
	if (i%2==0):
		str=str+x[i].upper()
	else:
		str=str+x[i].lower()
	i+=1
print("REVERSE STRING IS : ",str)
