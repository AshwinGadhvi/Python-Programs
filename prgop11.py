li=[1,2,3,4,5,6,7,8,9,10]
li2=[]
for i in range(len(li)):
    if(i<len(li)-1):
        li[-i],li[-i-1]=li[-i-1],li[-i]
print(li)

li3=[10,20,30]
li.insert(len(li),li3[-1])
print(li)

li3.append(li.pop())
print(li3)