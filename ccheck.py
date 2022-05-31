worddict={"dwivedi":119,"devil":43,"himanshu":90}
l=sorted(worddict.items(), key=lambda x:x[1])
print(l)
for i in l:
    print(i[0] , ":" , i[1] )
    
