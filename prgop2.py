li=[30,20,10,40,50,60,701,2,2,3,3,3,3,3]
li2=[]
for i in range(len(li)):
    li2.insert(i,li[-1])
    li.pop(-1)
print(li2)