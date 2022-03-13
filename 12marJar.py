n=int(input("THERE ARE 10 BALLS IN A JAR \n ENTER THE NO. OF BALLS YOU WANT TO PICK : "))
if(n>5):	print("sorry this is not a valid choice you cannot pick more than 5")
else:	print("after picking ",n," balls there are ",10-n," balls left in the jar")
