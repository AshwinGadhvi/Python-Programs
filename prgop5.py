li=[]
li2=[]
for i in range(0,4):
    li.insert(i,(input("Enter name : ")))
print(li)
for i in li:
    i=i.replace(i[0],"",1)
    li2.append(i)
print(li2)
