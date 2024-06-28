li=[]
li2=[]
for i in range(65, 91):
    for j in range(65,i+1):
        li.insert(i,str(chr(i)))
    li2=li
    print(" ")
print(li,end=" ")
print("***************")
print(li2)