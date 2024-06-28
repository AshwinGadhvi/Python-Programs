li=[10,20,30,40,50]
n=20
ans=0
for i in li:
    if n in li:
        ans=li.index(n)
    else:
        ans="number not found"
print("index of n is : ",li.index(n) )