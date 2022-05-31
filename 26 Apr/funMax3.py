def max(a,b,c):
     z=0
     if a>b:
          if a>c:
               z=a
          else :
               z=c
     else:
          if b>c:
               z=b
          else :
               z=c
     return z
p=int(input("enter : "))
q=int(input("enter : "))
r=int(input("enter : "))
print("The maximum among 3 nos. is ",max(p,q,r))
