def strong(t):
     f=1
     while(t!=0):
         f*=t
         t-=1
     return f
n=int(input("enter : "))
fact=strong(n)
print("Factorial =",fact)
