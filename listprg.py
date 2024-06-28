li=[10,20,30,20,40,40,50]
print(li)
result=[]
for a in (li):
    if(a not in result):
        result.append(a)
print(result)
