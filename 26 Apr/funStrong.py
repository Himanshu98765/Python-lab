def strong(n):
     sum=0
     while(n!=0):
         t=n%10
         f=1
         while(t!=0):
              f*=t
              t-=1
         sum+=f
         n//=10
     return sum
a=int(input("enter"))
fact=strong(a)
if(fact==a):
     print("it is a strong no.")
else: print("it is not a strong no.")
