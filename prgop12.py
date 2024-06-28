li=[10,20,30,40,50]
li2=[5,4,3,2,1]
li3=[]
li3=[li[i]/li2[i] for i in range(len(li))]
print(li3)
print(min(li3))