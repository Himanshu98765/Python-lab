n=int(input())
list=[]
sum1=0
for i in range(n):
	x=int(input())
	list.insert(i,x)
	if(i%2==0):
		sum1+=list[i]
print("sum = ",sum1)
