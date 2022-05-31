n=int(input("Enter the money to be withdrawn : "))
h=1
a=n-100
th=a//2000
rem=a%2000
five=rem//500
r=rem%500
h+=r//100

print("The notes for %d amount with atleast a hundred note are as follows : "%n)
print("Number of 2000 notes : ",th)
print("Number of 500 notes : ",five)
print("Number  of hundred notes : ",h)
