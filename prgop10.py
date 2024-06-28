li=[1,2,3,4,5,6,7,8,9,10]
li2=[1,2,3,4,5,6,7,8,9,10]
li3=list([li[x]+li2[x] for x in range(len(li))])
print(li3)
