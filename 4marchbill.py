x=int(input("ENTER THE NO. OF UNITS : "))
if(x<=50):
	bill=x*(0.5)
elif(x<=150):
	bill=(50*0.5)+((x-50)*0.75)
elif(x<=250):
	bill=(50*0.5)+(100*0.75)+((x-150)*1.2)
elif(x>250):
	bill=(50*0.5)+(100*0.75)+(100*1.2)+((x-250)*1.5)
print("your total bill amount is : ",bill)
