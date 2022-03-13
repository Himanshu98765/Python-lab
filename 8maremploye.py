bs=int(input("ENTER THE BASIC SALARY : "))
if bs<10000:
	sal=(bs*.80)+(bs*.90)+bs
elif bs>10000 and bs<20000:
	sal=(bs*.85)+(bs*.90)+bs
else:
	sal=(bs*.95)+(bs*.95)+bs
print("THE TOTAL SALARY OF EMPLOYEE WITH HRA AND DA = ",sal)
