n=int(input())
list=[]
for i in range(n):
	x=int(input())
	list.insert(i,x)
print(list)
sum1=list[0]+list[n-1]
if(n%2==0):
	sum1+=list[(n//2)-1]+list[(n//2)]
else:
	sum1+=list[(n//2)]
print(sum1)
